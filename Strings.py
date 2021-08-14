a ="andre"
print(a[1])
print(a[::-1])
print(a[1:4:2])
print(a.isspace())#so se tiver espaço
print(a.lower())
print(a.upper())
print(a.split())
print(a.split('a'))
print('empresa %s de IA' %(a))
b=1.7585
print('empresa %1.2f de IA' %(b)) #mostrar valores apos a virgula
print ('a:{A}, b:{B}, c:{C}'.format(A=1,B='Andre',C=1.89))
lista = [1,2,3, 'andre']
print(lista)
print(lista[0])
print(lista[:2])
print(lista[-1])
lista2 = ['a','b','c']
print(lista+lista2)
lista3 = lista+lista2
print(lista3)
lista+=[5]#add lista
print(lista)
print(len(lista))#comprimento
lista.append(9)#add lista
print(lista)
lista.pop()#remover o ultimo dado da lista
print(lista)
lista.pop(3)
print(lista)
print(lista.index(3))
lista.reverse()
print(lista)
lista.sort()#ordenar crescente
print(lista)
print(lista[::-1])

l1 = [1,2,3]
l2 =  [4,5,6]
l3 = [7,8,9]
m =[l1,l2,l3]
print(m)
print(m[0][2])
print(type(m))
#DICIONARIO
dicionario = {'chaves':1.2,'chave2':'andre'}
print(dicionario)
print(type(dicionario))
print(dicionario['chaves'])
print(type(dicionario['chaves']))
dicionario['chave3']=[1,2,3]
print(dicionario['chave3'])
print(dicionario.keys())
print(dicionario['chave3'][1])
dicionario['novo']={'dados': 123}
print(dicionario)
print(list(dicionario.keys()))#transf em lista
print(list(dicionario.values()))
print(dicionario.items())

#TUPLAS(não pode ser mudadas) mesma coisa que uma lista
t = (1,2,3,3,3)
print(t[1])
print(t.index(2))
print(t.count(3))
x = set()
x.add(5)
x.add(7)
x.add(9)
x.add(9)
print(x)
lista4=[1,1,1,2,2,5,86,4,2,2]
x = list(set(lista4))#lista
print(x)

'''
if case1:
    roda codigo
elif case2:
    roda codigo
elif case3:
    roda codigo
else:
    roda codigo
'''
if 1==1:
    print('caso 1')
elif 2==3:
    print('caso 2')
elif 2!=3:
    print('caso3')
else:
    print('nenhuma opção')
