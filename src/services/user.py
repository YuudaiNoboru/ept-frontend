from httpx import HTTPStatusError

from schemes.user import User
from services.client_api import client_api
from util.exception import APIError


async def create_new_user(nome: str, email: str, senha: str):
    data = {'username': nome, 'email': email, 'password': senha}
    try:
        async with client_api.get_client() as client:
            response = await client.post('/users/', json=data)
            response.raise_for_status()
            user = User(**response.json())
            return user
    except HTTPStatusError as e:
        msg_error = e.response.json().get('detail')
        raise APIError(msg_error)


async def login_user(email: str, senha: str):
    try:
        await client_api.authenticate(email, senha)
        print(client_api.token)
    except HTTPStatusError as e:
        msg_error = e.response.json().get('detail')
        raise APIError(msg_error)
