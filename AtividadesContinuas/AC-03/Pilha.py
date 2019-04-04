class Pilha:
    
    def __init__(self):
        self.__valores = []

    def get_valores(self):
        return self.__valores

    def set_valores(self, value):
        self.__valores.append(value)

    def empilhar(self, valor):
        self.set_valores(valor)

    def desempilhar(self):
        return self.get_valores().pop(0)

    def __str__(self):
        return f"Pilha({str(self.get_valores())})"
