import requests

def gerar_perfil():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']

        print("👤 Perfil Aleatório Gerado:")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"País: {pais}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao acessar a API:", erro)

# Executa a função
gerar_perfil()
