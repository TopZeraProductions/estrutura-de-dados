class Person():
    def __init__(self):
        self.__name      = ""
        self.__telephone = []
        self.__dateBirth = None
        self.__Mother    = None

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def telephone(self):
        return self.__telephone

    @telephone.setter
    def telephone(self, value):
        self.__telephone.append(value)

    @property
    def dateBirth(self):
        return self.__dateBirth

    @dateBirth.setter
    def dateBirth(self, value):
        self.__dateBirth = value

    @property
    def Mother(self):
        return self.__Mother

    @Mother.setter
    def Mother(self, newObj):
        self.__Mother = newObj


Son = Person()
Son.name             = "Joao"
Son.dateBirth        = "12/01/1998"
Son.telephone        = "+5511953377823"

Son.Mother = Person()
Son.Mother.name      = "Lenilda"
Son.Mother.telephone = "+5511952371890"
Son.Mother.dateBirth = "18/11/1976"

print(Person.name,"\n",Person.telephone,"\n",Person.dateBirth)
print(Person)