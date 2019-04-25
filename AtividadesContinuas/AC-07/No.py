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
