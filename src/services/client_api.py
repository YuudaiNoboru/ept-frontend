from contextlib import asynccontextmanager

import httpx

from util.settings import settings


class APIClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.token = None

    async def authenticate(self, username: str, password: str):
        """Autentica o usuário e armazena o token."""
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            response = await client.post(
                'auth/token',
                data={'username': username, 'password': password},
                headers={'Content-Type': 'application/x-www-form-urlencoded'},
            )
            response.raise_for_status()
            self.token = response.json().get('access_token')

    @asynccontextmanager
    async def get_client(self):
        """Retorna um cliente HTTP configurado com autenticação."""
        async with httpx.AsyncClient(base_url=self.base_url) as client:
            if self.token:
                client.headers.update({
                    'Authorization': f'Bearer {self.token}'
                })
            yield client  # Agora "client" é o httpx.AsyncClient


client_api = APIClient(settings.BASE_URL_API)
