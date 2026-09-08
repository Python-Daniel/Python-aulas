#Dicionario sao colecoes do tipo formulario
# chave:valor
# Exemplo
# Nome : Moita
# Idade : 18
# Sexo : Masc
# NAO SAO POSICIONAIS - nao tem indice
# permitem tipos de dados diferentes
# permitem valores repetidos, porem chaves SAO UNICAS
# permitem inclusao, alteracao, exclusao SAO MUTAVEIS
# simbolo sao as {}
 
print('Dicionarios')
aluno = {'nome': 'Daniel', 'idade': 18, 'sexo': 'masculino'}
print(aluno)
print(type(aluno))
 
print('Acessando valor a valor')
print(aluno['nome'])
print(aluno['idade'])
print(aluno['sexo'])
 
print('Dicionario vazio')
vazio = {}
print(vazio)
 
print('\nAcrescentando valores em um dicionario')
vazio['categoria'] = 'Brinquedos'
print(vazio)
 
print('\n')
aluno['profissao'] = 'estagiario'
print(aluno)
 
print('\nAlterando valores')
aluno['nome'] = 'Daniel'
print(aluno)
print(aluno.get('nome'))
aluno.update({'idade' : 18})
print(aluno)
 
print('\nRemovendo valores')
aluno.pop('idade') #elimina segundo uma chave
print(aluno)
del aluno['sexo'] #elimina uma chave, del é uma exclusao generica
print(aluno)
aluno.popitem()
print(aluno)
 
print('\nLimpa o dicionario')
aluno.clear()
print(aluno)
 
###ATENCAO###
#Consigo sempre alterar valores
#Mas nunca chaves
aluno = {'nome': 'Daniel', 'sexo': 'masculino', 'profissao': 'estagiario'}
print(aluno)
aluno['profissao'] = 'analista junior'
print(aluno)
#aqui ele nao troca, ele acaba acrescentando um valor no dicionario
aluno['profissao carteira'] = 'analista junior'
print(aluno)
#como trocar a chave, precisa eliminar e recriar
del aluno['profissao carteira']
aluno.pop('profissao')
aluno['profissao carteira'] = 'analista junior'
print(aluno)
 
print('\nPercorrendo ou varrendo o dicionario')
aluno = {'nome': 'Daniel', 'idade': 18, 'sexo': 'masculino', 'profissao carteira': 'analista junior'}
for caracteristicas in aluno:
    print(caracteristicas)
print('\nSomente as chaves')
for chave in aluno.keys():
    print(chave)
print('\nSomento os valores')
for valor in aluno.values():
    print(valor)
print('\nSomente os valores pela chaves')
for chave in aluno:
    print(aluno[chave])
 
print('\nOs itens completos')
for item in aluno.items():
    print(item)
print('\nOs itens ja separados com atribuicao multiplos')
for chave, valor in aluno.items():
    print(f'{chave} = {valor}')

    #atribuicao multipla
    x, y, z = 0, 1, 2
    print(f'{x}')
    print(f'{y}')
    print(f'{z}')

    # na maior parte das colecoes a copia se da pela igualdade
    #vamos examinar a lista
    print('\n\n')
    original = ['cafe', 'pao', 'leite']
    copiafalsa = original
    copia = original
    print('original', original)
    print('copia', copia)
    copia.append('cachorro')
    copiafalsa.append('cachorro')
    copia.append('gato')
    print('original ', original)
    print('copia ', copia)
    print('copialfalsa', copiafalsa)

print('\nCopiando o dicionario')
aluno = {'nome': 'Daniel', 'idade': 18, 'sexo': 'masculino', 'profissao carteira': 'analista junior'}
aluno_copia = aluno.copy()
aluno_copia['nome'] = ('Andrea Macedo')
print(aluno)
print(aluno_copia)