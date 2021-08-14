print(type(1))
print(type([]))
print(type(()))
print(type({}))

#instancia da class list(objeto)
l = [1,2,3]

print('----------------------------')

class Dog(object):
    #construtor
    def __init__(self, raca):
        self.raca = raca #public
       #self.__raca = raca #privado

rex = Dog('vira-lata')
print(rex.raca)

print('----------------------------')

class Dog(object):
    especie = 'mamifero'
    #construtor
    def __init__(self, raca):
        self.raca = raca #public
       #self.__raca = raca #privado

rex = Dog('vira-lata')
print(rex.raca)
print(rex.especie)

print('----------------------------')

class Circulo(object):
    pi = 3.14
    # se nao passar nenhum valor, vale 1
    def __init__(self, raio=1):
        self._raio = raio
    def area(self):
        return self._raio * self._raio * Circulo.pi
    #caso os valores sejam privados
    def setraio(self, raio):
        self._raio = raio
    def getraio(self):
        return self._raio
circulo = Circulo(raio=2)
print(circulo.area())
circulo.setraio(8)
print(circulo.getraio())

circulo2 = Circulo(6)
print(circulo2.area())

print('----------------------------')
#Herança

#Classe PAI
class Animal(object):
    def __init__(self):
        print('Animal Criado')
    def sou(self):
        print('Animal')
    def comer(self):
        print('comendo')

#Classe FILHO
class Dog(Animal):
    def __init__(self):
        #super().__init__() pode usar esse tbm
        Animal.__init__(self) #ou esse
        print('Cachorro criado')
    def sou(self):
        print('Dog')
    def latir(self):
        print('Au au')
d = Dog()
d.sou()
d.comer()
d.latir()

print('----------------------------')
#Metodos Especiais

class Livro(object):
    def __init__(self, titulo, autor, paginas):
        print('Livro criado')
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return 'titulo: %s, autor: %s, paginas: %s' %(self.titulo, self.autor, self.paginas)
    def __len__(self):
        return self.paginas
    def __del__(self):
        print('livro destruido')
livro = Livro('Python','Luciano', 799)
print(livro)
print(len(livro))
del livro

print('----------------------------')

#Atividade

'''crie uma classe Retangulo com os parametros inteiro base e inteiro altura. E os metodos Perimetro e area'''
class Retangulo(object):
    def __init__(self, base=0, altura=0):
        self._base = base
        self._altura = altura
    def setBase(self,base):
        self._base
    def setAltura(self,altura):
        self._altura
    def getBase(self):
        return self._base
    def getAltura(self):
        return self._altura
    def Perimetro(self):
        return 2*self._base + 2* self._altura
    def Area(self):
        return self._base*self._altura

try:
    b = float(input('Base: '))
except ValueError:
    print('Valor Invalido')
try:
    h = float(input('Altura: '))
except ValueError:
    print('Valor Invalido')
retangulo = Retangulo(b,h)

print('Perimetro: %.2f' %retangulo.Perimetro())
print('Area: %.2f' %retangulo.Area())

print('----------------------------')

'''Trabalho usando heranças - alunos e materia'''
