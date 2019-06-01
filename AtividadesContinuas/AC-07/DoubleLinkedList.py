class Node:
    def __init__(self, arg):
        self.__value = arg
        self.__prev = None
        self.__next = None

    def get_value(self):
        return self.__value

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

    def get_prev(self):
        return self.__prev

    def set_prev(self, node):
        self.__prev = node

    def __str__(self):
        prev, next = "None", "None"
        if self.get_prev() is not None:
            prev = "*" + str(self.get_prev().get_value())

        if self.get_next() is not None:
            next = "*" + str(self.get_next().get_value())

        # return "&{" + prev + ", " + str(self.get_value()) + ', ' + next + "}"

        return "No(" + str(self.get_value()) + ")"

    def __repr__(self):
        return '%s' % (hex(id(self)))


class DoubleLinkedList:
    def __init__(self):
        self.__start = None
        self.__end = None

    def add(self, node):
        if self.__start is None:
            self.__start = node

        antes = self.__end
        if self.__end is not None:
            antes = self.__end
            self.__end.set_next(node)

        self.__end = node
        self.__end.set_prev(antes)

    def add_single(self, node):
        if self.__start is None:
            self.__start = node

        if self.__end is not None:
            self.__end.set_next(node)

        self.__end = node

    def remove(self, value):
        if self.__start.get_value() == value:
            self.__start = self.__start.get_next()

        anterior = self.__start
        no = self.__start

        while no is not None:
            if no.get_value() == value:
                anterior.set_next(no.get_next())

            swap = anterior
            anterior = no
            no = swap.get_next()

    def __str__(self):
        result = []
        no = self.__start

        while no is not None:
            result.append(str(no))
            no = no.get_next()

        return "[" + ", ".join(result) + "]"


lista = DoubleLinkedList()
lista.add(Node(1))
lista.add(Node(2))
lista.add(Node(3))
lista.add(Node(4))
lista.add(Node(5))

print(lista)

lista.remove(5)
print(lista)
lista.remove(4)
print(lista)
lista.remove(1)
print(lista)
lista.remove(3)
print(lista)
lista.remove(2)
print(lista)

'''
A saída do programa deve ser:
[No(10), No(20), No(30), No(40)]
[No(20), No(30), No(40)]
[No(20), No(30), No(40)]
[No(20), Noy(30)]
[No(20)]
[]
'''