lista = [0,1,2,3,4,5,6,7,8,9]
tupla = (0,1,2,3,4,5,6,7,8,9)
'''for item in objeto:
    fazer algo'''
for dados in lista:
    print(dados)

print('------------------------------------')

string= 'fazer algo'
for dados in string:
    print(dados)

print('------------------------------------')

for t in tupla:
    print(t)

print('------------------------------------')

tupla = [(0,1),(2,3),(4,5),(6,7),(8,9)]
for t1, t2 in tupla:
    print(t1,t2)

print('------------------------------------')

x=0
while x < 10:
    print(x)
    x+=1

print('------------------------------------')

y=0
l=[]
while y < 10:
    l.append(y)
    y+=1
    print(l)
    if y ==5:
        break
    print(l )


print('------------------------------------')

z=0
m=[]
while z < 10:
    if z == 5:
        z+=1
        continue
    m.append(z)
    z+=1
    print(m)

print('------------------------------------')

print(range(0,1000))

for i in range(0,1000):
    print(i)

print('------------------------------------')

for j in range(0,1000,5):
    print(j)

print('------------------------------------')

c = []
for i in range(0, 10):
    c.append(i)
print(c)

x=[i for i in range(0,10)]
print(x)

x = [i for i in range(0, 20) if i % 5 == 0]
print(x)

'''Uma pessoa vai fazer uma compra em uma festa junina, a pessoa vai comprar 4 fichas de o valor final para pessoa com os preços do dicionário. 
{'pipoca' : 1.50, 'cachorro quente' : 3.50, 'pescaria' : 3.00, 'caldo : 5.00, 'quentão' : 8.00, 'pé-de-moleque': 10}'''

'''fichas = {'pipoca' : 1.50, 'cachorro quente' : 3.50, 'pescaria' : 3.00, 'caldo' : 5.00 ,'quentao' : 8.00, 'pe-de-moleque': 10}
x = 0
for i in range(4):
    compra = input('Quais fichas você quer? ')
    x += fichas[compra]
print(str(x))'''

'''Faça a conversão das temperaturas de Celsius para Fahrenheit
Formula: F = C x 1,8 + 32
Celsius = [0, 10, 15, 20, 30, 50, 100]'''

'''c = [0, 10, 15, 20, 30, 50, 100]
f= []
for x in c:
    f.append(x*1.8+32)
print(f)'''
