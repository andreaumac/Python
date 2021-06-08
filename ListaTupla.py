lista = [1,2,3,5,7]
lista_animal = ['cão', 'gato', 'passáro']
print(type(lista))
print(lista)

#acessar o valor na posição
print(lista_animal[0])

#percorrer a lista
for x in lista_animal:
    print(x)
#percorrer a lista e somar o valores int
soma = 0
for y in lista:
    print(y)
    soma+=y
print(soma)

#somar a lista resumido
print(sum(lista))

#ver se existe na lista
if 'lobo' in lista_animal:
    print('Existe na lista')
else:
    print('Não existe')

#incluir na lista
lista_animal.append('lobo')
print(lista_animal)

#retirar ultimo(pilha)
lista_animal.pop()
#remover pelo nome
lista_animal.remove('gato')

print(lista_animal)

#oedenar a lista
lista_teste = [1,50,23,25,15,11,56,44]
lista_teste.sort()
print(lista_teste)

print('--------------------------------')
#tupla é imutavél
tupla = (1,10,12,14)
print(tupla)
#tupla[0] = 12 nao funciona
#len quantos elementos tem
print(len(tupla))

#converter para tuple
tupla_animal = tuple(lista_animal)
print(type(tupla_animal))

#converter para lista
list_animal = list(tupla_animal)
print(type(list_animal))