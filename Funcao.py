'''def nome_da_funcao():
    #codigo que vai roda
    return #retornar um resultado'''

def ola():
    print('Ola')
ola()

def ola(nome):
    print('Ola %s' %(nome))
ola('Andre')

def soma(n1, n2):
    return n1 + n2
x = soma(5,8)
print(x)

def soma(n1, n2):
    res = n1 + n2
    print(res)
soma(5,8)

#raramente usado
def soma(n1, n2):
    def res(valor):
        print(valor)
    valor = n1+n2
    res(valor)
soma(5,8)

print('------------------------------')

def soma2(n1,n2):
    valor = n1+n2
    return valor
x=5

def sub(y):
    global x #variavel global
    return x - y
f = sub(2)
print(f)

print('------------------------------')

#object.method(arg)
l = [1,2,3,4,5]
print(l)
l.append(6)
print(l)
l.pop()
print(l)
l.reverse()
print(l)

print('------------------------------')

#TRATAMENTO DE ERRO

'''print(int('a'))#erro'''
try:
    print('a')
    int('a') #não pode ser convertido em int
#except ValueError:
    #print('O valor não pode ser convertido')
except Exception as e:#mostra o erro
    print(e)
else:
    print('funcionou') #caso nao der erro
finally:
    print('qualquer forma ele executa')

print('------------------------------')

'''try:
    a = input('digite um valor: ')
    int(a)
except ValueError:
    print('O valor não pode ser convertido')
except Exception as e:  # mostra o erro
    print(e)
finally:
    print('qualquer forma ele executa')'''

print('------------------------------')

#EXERCICIOS

'''Crie uma função para converter graus Celsius em fahrenheit.'''

def converter(c):
    return c*1.8+32

celsius = [0,10,15,20,30,50,100]
f = []

for x in celsius:
    f.append(converter(x))
print(f)

'''Crie uma função para fazer uma soma de 5 números.'''
def soma(n):
    soma=0
    for x in n:
        soma+=x
    return soma
print('Digite um valor: ')
n=[]
for i in range(5):
    n.append(int(input()))
print(str(soma(n)))

'''Crie uma função que resolva uma equação de primeiro grau com tratamento de erro.
y = ax+b'''

'''try:
    a = float(input('Digite o "a" da função: '))
    b = float(input('Digite o "b" da função: '))

    def primeiro_grau(a,b):
        y = 0
        x = (y-b)/a
        return x
except ValueError as e: #Tratamento de erro
    print('ERRO')
else:
    res = primeiro_grau(a,b)
    print(res)'''

'''ax+b = 0
x = -b/a'''
def grau1(a,b):
    if (a != 0):
        y = -b/a
    else:
        y= 'O valor de a não pode ser 0'
    return y
try:
    a = int(input('Digite o valor de a: '))
except ValueError:
    print('Valo de a não e um numero')
try:
    b = int(input('Digite o valor de b: '))
except ValueError:
    print('Valo de b não e um numero')
try:
    y = grau1(a,b)
    print(y)
except Exception as e:
    print("Digite o valor correto para 'a' e 'b'")