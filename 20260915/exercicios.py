#Ex1
try:
    numero = int(input("Digite um número inteiro: "))
    quadrado = numero ** 2
    print(f"O quadrado de {numero} é {quadrado}.")

except ValueError:
    print("Erro: o valor informado não é um número inteiro.")


#Ex2
class NumerosIguaisError(Exception):
    pass


try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    if numero1 == numero2:
        raise NumerosIguaisError("Os dois números são iguais.")

    if numero1 > numero2:
        print(f"Maior: {numero1}")
        print(f"Menor: {numero2}")
    else:
        print(f"Maior: {numero2}")
        print(f"Menor: {numero1}")

except ValueError:
    print("Erro: digite números válidos.")

except NumerosIguaisError as erro:
    print(f"Comparação encerrada: {erro}")


#Ex3
try:
    letra = input("Digite uma letra entre A, B, C ou D: ").upper()

    frutas = {
        "A": "Abacaxi",
        "B": "Banana",
        "C": "Cereja",
        "D": "Damasco"
    }

    if letra not in frutas:
        raise ValueError("A letra informada não é válida.")

    print(f"Fruta: {frutas[letra]}")

except ValueError as erro:
    print(f"Erro: {erro}")

#Ex4
try:
    salario_minimo = float(input("Digite o valor do salário mínimo: "))
    salario = float(input("Digite o salário da pessoa: "))

    if salario_minimo < 0:
        raise ValueError("O salário mínimo não pode ser negativo.")

    if salario < 0:
        raise ValueError("O salário não pode ser negativo.")

    quantidade = salario / salario_minimo

    print(f"A pessoa ganha {quantidade:.2f} salários mínimos.")

except ValueError as erro:
    print(f"Erro: {erro}")

except ZeroDivisionError:
    print("Erro: o salário mínimo não pode ser zero.")


#Ex5
def buscar_item_por_indice(lista: list[str], indice: int) -> str:
    return lista[indice]


produtos = [
    "Notebook",
    "Smartphone",
    "Tablet",
    "Fone de ouvido",
    "Teclado"
]

try:
    indice = int(input("Digite o índice do produto: "))

    produto = buscar_item_por_indice(produtos, indice)

    print(f"Produto em promoção: {produto}")

except ValueError:
    print("Erro: o índice deve ser um número inteiro.")

except IndexError:
    print("Erro: a posição informada não existe na lista.")


#Ex6
produtos = {
    "Notebook": 3500.00,
    "Smartphone": 1800.00,
    "Tablet": 1200.00,
    "Fone de ouvido": 250.00,
    "Teclado": 150.00
}

try:
    nome = input("Digite o nome do produto: ")

    preco = produtos[nome]

    print(f"O preço do {nome} é R$ {preco:.2f}.")

except KeyError:
    print("Erro: o produto não está cadastrado.")


#Ex7
try:
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    media = (numero1 + numero2) / 2

except ValueError:
    print("Erro: digite apenas números válidos.")

else:
    print(f"A média é {media:.2f}.")
    print("Cálculo realizado com sucesso!")

finally:
    print("Cálculo finalizado.")
