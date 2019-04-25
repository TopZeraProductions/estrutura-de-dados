class No:
    def __init__(self, numero):
        self.__valor = numero
        self.__proximo = None

    def getValor(self):
        return self.__valor

    def getProximo(self):
        return self.__proximo

    def setProximo(self, No):
        self.__proximo = No

    def __str__(self):
        return 'No(' + str(self.__valor) + ')'


class ListaLigada:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def add(self, no):
        if self.__inicio is None:
            self.__inicio = no

        if self.__fim is not None:
            self.__fim.setProximo(no)

        self.__fim = no

    def remove(self, value):
        if self.__inicio.getValor() == value:
            self.__inicio = self.__inicio.getProximo()

        anterior = self.__inicio
        no = self.__inicio

        while no is not None:
            if no.getValor() == value:
                anterior.setProximo(no.getProximo())

            swap = anterior
            anterior = no
            no = swap.getProximo()

    def __str__(self):
        result = []
        no = self.__inicio

        while no is not None:
            result.append(str(no))
            no = no.getProximo()

        return "[" + ", ".join(result) + "]"


lista = ListaLigada()

lista.add(No(10))
lista.add(No(20))
lista.add(No(30))
lista.add(No(40))
print(lista)

lista.remove(10)
print(lista)

lista.remove(50)
print(lista)

lista.remove(40)
print(lista)

lista.remove(30)
print(lista)

lista.remove(20)
print(lista)


'''
A saída do programa deve ser:
[No(10), No(20), No(30), No(40)]
[No(20), No(30), No(40)]
[No(20), No(30), No(40)]
[No(20), No(30)]
[No(20)]
[]
'''