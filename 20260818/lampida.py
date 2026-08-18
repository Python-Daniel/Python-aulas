#Lambida
#Funcao anonima (pequena - de uma linha só-função inLine)
#A criacao da funcao esta proxima do uso 
#Versateis
#cuidado que temos que ter,é NAO RESOLVER TUDO COM LAMBIDA
#Se vc fizer isso seu programa fic ailegivel 


def dobro (n:int) -> int:
    '''
    calcula o dobrode um numero inteiro
    
    :param n: numero inteiro
    :return: dobro de um numero inteiro
    
    '''
    return n * 2

#uso 
print (dobro(4))

#transformar em lambida
#sintaxe lambda <argumentos/parametro> : <expressao de retorno>
#lambda SEMPRE TEM UM RETURN
ldobro= lambda n : n * 2
print(ldobro(79))
# o uso mais comum 
print((lambda n : n * 2)(65))


#Lambda CONDICIONAL
#Te, um if embutido

#funcao que decide qual o maior de 2 numero 
def maior(x:int,y:int) ->int:
    if x > y:
        return x 
    else:
        return y
    

# transformando em lambda
lmaior = lambda x, y: x if x > y else y

print(lmaior(y=4, x=5))

# uso mais comum
print((lambda x, y: x if x > y else y)(9, 65))

# posso usar o print dentro do lambda
# pode, mas cuidado
lmenor = lambda x, y: print(x) if x < y else print(y)

xpto = lmenor(123, 97)
lmenor (43,2)

#a melhor solucao
lmenor2 = lambda x, y: f'entre {x} e {y} o numero menor é {x}' if x < y else f'entre {x} e {y} o numero menor é {y}'
print(lmenor2(8,23))


#map é uma funcionalidade do python que permite aplicar
#uma funcao em todos os elementos de uma coleção 

def dobro (n:int) -> int:
    return n * 2
numeros = [7, 87, 90, -23, 4, 0]

# da maniera roots
dobrados = []
for n in numeros:
    dobrados.append (dobro(n))
    print (numeros)
    print(dobrados)

    print('\nCom o map')
    #com o map
    dobrados2 = list(map(dobro,numeros))
    print(dobrados2)
    #2o uso de direto no print
    print(list(map(dobro, numeros)))

    print('\nCom map e com Lambda')
    #utilizando o ldobro abaixo, como eu faria o map?
    ldobro = lambda n :n * 2
    dobrados3 = list(map(dobro, numeros))
    print(dobrados3)

    #o jeito mais pythoneiro
    print(list(map((lambda n : n*3, [23,4,874,4]))))