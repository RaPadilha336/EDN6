import requests

def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        if "erro" in dados:
            print("❌ CEP não encontrado. Verifique e tente novamente.")
            return

        print("📍 Endereço encontrado:")
        print(f"Logradouro: {dados.get('logradouro', 'N/A')}")
        print(f"Bairro: {dados.get('bairro', 'N/A')}")
        print(f"Cidade: {dados.get('localidade', 'N/A')}")
        print(f"Estado: {dados.get('uf', 'N/A')}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao consultar o CEP:", erro)

# Entrada do usuário
cep_input = input("Digite o CEP (somente números): ").strip()
if cep_input.isdigit() and len(cep_input) == 8:
    consultar_cep(cep_input)
else:
    print("⚠️ CEP inválido. Certifique-se de digitar 8 números.")
