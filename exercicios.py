#7. Use list comprehension para criar uma lista
#com os quadrados dos numeros de 1 a 10

quadrados = [ n ** 2 for n in range(1, 11)]
print (quadrados)
('\nList comprehension')

#7.a
#Peca o numero inicial ao usuario, peca o numero final
#usando list comprehension, calcule os quadrados dos numeros 
#entre o numero inicial e o numero final

inicial = int(input('Digite seu numero inicial'))
final = int(input('Digite o seu numero final'))
quadrados = [n ** 2 for n in range(inicial, final+1)]
print (quadrados)

numeros = [3, 8, 15, 22, 7, 40, 11]
pares = [n for n  in numeros if n % 2 == 0]
print(pares)