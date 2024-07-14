import requests

def obter_dados_moedas():
    url = "https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

def mostrar_valores(dados_moedas):
    if dados_moedas:
        conversao_bitcoin_real = dados_moedas["BTCBRL"]["bid"]
        conversao_dolar_real = dados_moedas["USDBRL"]["bid"]
        conversao_euro_real = dados_moedas["EURBRL"]["bid"]

        ultima_atualizacao_bitcoin_real = dados_moedas["BTCBRL"]["create_date"]
        ultima_atualizacao_dolar_real = dados_moedas["USDBRL"]["create_date"]
        ultima_atualizacao_euro_real = dados_moedas["EURBRL"]["create_date"]

        print(f"\nO valor do bitcoin está: R${conversao_bitcoin_real}, última atualização em {ultima_atualizacao_bitcoin_real}")
        print(f"\nO valor do dólar está: R${conversao_dolar_real}, última atualização em {ultima_atualizacao_dolar_real}")
        print(f"\nO valor do euro está: R${conversao_euro_real}, última atualização em {ultima_atualizacao_euro_real}")

def saudacao_cliente():
    print("Olá, seja bem-vindo(a) ao nosso consultor de valores das moedas!")

def main():
    saudacao_cliente()
    dados_moedas = obter_dados_moedas()
    mostrar_valores(dados_moedas)
    while True:
        opcao = input("\nDeseja atualizar os valores? (s/n): ").strip().lower()
        if opcao == 's':
            dados_moedas = obter_dados_moedas()
            mostrar_valores(dados_moedas)
        elif opcao == 'n':
            print("Até a próxima!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()