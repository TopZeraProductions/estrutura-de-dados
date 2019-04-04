class Fila:

    def __init__(self):
        self.__valores = []

    def get_valores(self):
        return self.__valores

    def set_valores(self, value):
        self.__valores.append(value)

    def enfileirar(self, valor):
        self.__valores.append(valor)

    def desenfileirar(self):
        return self.get_valores().pop(0)

    def __str__(self):
        return f"Fila({str(self.get_valores())})"
