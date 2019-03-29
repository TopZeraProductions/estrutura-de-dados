class Ponto():
    def __init__(self, x, y):
        self.__ponto_x = x
        self.__ponto_y = y

    def show_points(self):
        print(self.__ponto_x,self.__ponto_y)

p = Ponto(5,10)
p.show_points()

class Container():
    def __init__(self, arg):
        self.__valor = arg

    def get_valor(self):
        return self.__valor

    @staticmethod
    def of(value):
        return Container(value)

    def map(self, fn):
        if self.get_valor() == None:
            return None

        return Container(fn(self.get_valor()))


contai = Container.of(15)
print(contai.get_valor())

def sqrt(val):
    return val * val

container_2 = contai.map(lambda valor : valor * 3.14)
container_3 = contai.map(sqrt)

print(container_2.get_valor())

class Fila():
    def __init__(self):
        self.__valores = []
        self.get_valores = lambda     : self.__valores
        self.enfileirar  = lambda arg : self.__valores.append(arg)

    def desfileirar(self):
        if len(self.__valores) > 0:
            del self.__valores[0]

fila = Fila()
fila.enfileirar(5)
fila.enfileirar(8)
fila.enfileirar(12)
print(fila.get_valores())
fila.desfileirar()
print(fila.get_valores())

class Pilha():
    def __init__(self):
        self.__valores   = []
        self.get_valores = lambda : self.__valores

    def empilhar(self, arg):
        self.__valores.append(arg)

    def Desenpilhar(self):
        if len(self.__valores) > 0:
            val = self.__valores[len(self.__valores) - 1]
            del self.__valores[len(self.__valores) - 1]
            return val

fila = Pilha()
fila.empilhar(5)
fila.empilhar(8)
fila.empilhar(12)
print(fila.get_valores())
fila.Desenpilhar()
print(fila.get_valores())