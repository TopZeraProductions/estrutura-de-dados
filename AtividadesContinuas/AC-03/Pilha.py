class Pilha:
    
    def __init__(self):
        self.valores = []

    def empilhar(self, valor):
        self.valores.append(valor)

    def desempilhar(self):
        return self.valores.pop(-1)

    def __str__(self):
        return f"Pilha({str(self.valores)})"