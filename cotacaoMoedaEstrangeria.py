import requests

def consultar_cotacao(moeda):
    moeda = moeda.upper()
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada. Verifique o código e tente novamente.")
            return

        info = dados[chave]
        print("Cotação Atual:")
        print(f"Moeda: {info['name']}")
        print(f"Valor Atual: R$ {float(info['bid']):.2f}")
        print(f"Valor Máximo: R$ {float(info['high']):.2f}")
        print(f"Valor Mínimo: R$ {float(info['low']):.2f}")
        print(f"Data: {info['create_date']}")

    except requests.exceptions.RequestException as erro:
        print("Erro ao consultar a cotação:", erro)

# Entrada do usuário
moeda_input = input("Digite o código da moeda estrangeira (ex: USD, EUR, ARS): ").strip()
if moeda_input:
    consultar_cotacao(moeda_input)
else:
    print("Código de moeda inválido.")