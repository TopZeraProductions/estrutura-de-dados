class Fila:

    def __init__(self):
        self.valores = []

    def enfileirar(self, valor):
        self.valores.append(valor)

    def desenfileirar(self):
        return self.valores.pop(0)

    def __str__(self):
        return f"Fila({str(self.valores)})"