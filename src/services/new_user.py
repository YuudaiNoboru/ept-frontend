from services.client_api import client_api


async def create_new_user(nome: str, email: str, senha: str):
    data = {'username': nome, 'email': email, 'password': senha}
    async with client_api.get_client() as client:
        response = await client.post('/users/', json=data)

    print(response.text)
