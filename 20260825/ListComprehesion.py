print('Revisao map')
def dobro (n:int) -> int:
    return n * 2
numeros = [7, 87, 90, -23, 4, 0]

print (numeros)
numeros_dobrados = list(map(dobro, numeros))
print (numeros_dobrados)

def mult(n: int, m: int) -> int:
    return n * m

numeros = [7, 87, 90, -23, 4, 0]
multiplicadores = [2, 3, 4, 5, 6, 7]

multiplicados = list(map(mult, numeros, multiplicadores))
print(multiplicados)

multiplicados2 = list(map(lambda n, m: n * m, numeros, multiplicadores))
print(multiplicados2)

print('\nList Comprehension')

numeros = [7, 87, 90, -23, 4, 0]
dobrados = []
for n in numeros:
    dobrados.append(n * 2)

print (dobrados)
print('\nList Comprehension')
dobrados2 = [n * 2 for n in numeros]
print(dobrados2)




