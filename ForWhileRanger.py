
'''vai de 0 a 100'''
for x in range(90, 100):
    print(x)

#numeros primos
a = int(input('Entre com um número: '))
div = 0
for y in range(1, a+1):
    resto = a % y
    if resto == 0:
       div += 1
if div == 2:
    print('Primo')
else:
    print('Não é primo')


#numero primo informado pelo usuario
b = int(input('Valor: '))
for z in range(b+1):
#for z in range(101): 100 números primos
    divi = 0
    for w in range(1, z+1):
        rest = z % w
        if rest == 0:
            divi += 1
    if divi == 2:
        print(z)


#laço 0 a 9
print('--------------------------')
h = 0
while h < 10:
    print(h)
    h+=1
print('--------------------------')


#laço ate que uma afirmação seja verdadeira
nota = int(input('Entre com a nota menor que 10: '))
while nota>10:
    nota = int(input('Nota inválida. Entre com a nota menor que 10: '))