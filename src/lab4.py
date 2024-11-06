class Zoo:
    def init(self, vs_number = 0, name = None, an_number = 0, year = 0, type_of_animal = None):
        self.vs_number = vs_number
        self.__name = name
        self.__an_number = an_number
        #не приватні
        self.year = year
        self.type_of_animal = type_of_animal

    def get_vs_number(self):
        '''гетери'''
        return self.__vs_number

    def get_name(self):
        return self.__name

    def get_an_number(self):
        return self.__an_number

    def set_vs_number(self, new_vs_number):
        '''сетери'''
        self.__vs_number = new_vs_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_an_number(self, new_an_number):
        self.__an_number = new_an_number

    def __str(self):
        '''перевизначення методу str'''
        return (f"кількість відвідувачів: {self.vs_number}, "
                f"Назва '{self.__name}', "
                f"тварин: {self.__an_number}, "
                f"рік заснування: {self.year}, "
                f"тип тварин: {self.type_of_animal}")

    def __repr(self):
        '''перевизначення методу repr'''
        return (f"vs_number={self.vs_number}, "
                f"name='{self.__name}', "
                f"an_number={self.__an_number}, "
                f"year={self.year}, "
                f"type_of_animal='{self.type_of_animal}')")

    def __del(self):
        '''деструктор'''
        print(f"зоопарк '{self.__name}' знищений.")

def main():
    Zoo1 = Zoo(75000, "Київський зоопарк", 250, 1999, "птахи")
    Zoo2 = Zoo(100000, "Зоопарк 'ХII місяців'", 230, 1992, "савці")
    Zoo3 = Zoo(50000, "Черкаський зоопарк", 200, 2007, "риби")
    Zoo4 = Zoo()

    print(Zoo1)
    print(Zoo2)
    print(Zoo3)
    print(Zoo4)
#print(f"тільки кількість: {Zoo4.get_vs_number()}")
    print("---------------------------------------------------------------------------------------------")
    print(repr(Zoo1))
    print(repr(Zoo2))
    print(repr(Zoo3))
    print(repr(Zoo4))
main()