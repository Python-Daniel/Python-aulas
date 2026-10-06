#Consumo API
 
#Api serve para recuperarmos dados a partir da chamada de um programa
#Tipicamente esses "programas" estao disponiveis em alguma url
 
#Nossa aplicação --> requisicao para um servidor (API)
#Nossa aplicação <-- reposta
 
#Requisições são feitas atraves do REQUEST
#Quando usamos http usamos a biblioteca request
#pip install requests
#dinamica
#para fazer a requisição usamos requests.get
#e recebemos a resposta com resposta.json
 
#Tbm temos o status a resposta
#resposta.status_code --> 200 ok, 404 file not found, 500 internal server error

import requests
try:
    resposta = requests.get("https://viacep.com.br/ws/01001000/json/")
    if resposta.status_code == 200:
        dados = resposta.json()
        print(dados)
    else:
        raise Exception("Erro na requisição. Código de status:", resposta.status_code)

except requests.exceptions.ConnectionError as e:
    print("Ocorreu um erro de conexão:", e)

except Exception as e:
    print("Ocorreu um erro ao fazer a requisição:", e)