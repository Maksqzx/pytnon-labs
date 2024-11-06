class Zoo:
    def __init__(self, vs_number=0, name="", an_number=0, year=0, type_of_animal=""):
        self.__vs_number = vs_number
        self.__name = name
        self.__an_number = an_number
        # не приватні
        self.__year = year
        self.__type_of_animal = type_of_animal

    def get_vs_number(self):
        """гетери"""
        return self.__vs_number

    def get_name(self):
        return self.__name

    def get_an_number(self):
        return self.__an_number

    def set_vs_number(self, new_vs_number):
        """сетери"""
        self.__vs_number = new_vs_number

    def set_name(self, new_name):
        self.__name = new_name

    def set_an_number(self, new_an_number):
        self.__an_number = new_an_number

    def __str__(self):
        '''перевизначення методу str'''
        return f"name: {self.__name}"

    def __repr__(self):
        '''перевизначення методу repr'''
        return f"name: {self.__name}"


    def __del__(self):
        '''деструктор'''
        print(f"зоопарк '{self.__name}' знищений.")


def main():
    zoo1 = Zoo(75000, "Київський зоопарк", 250, 1999, "птахи")
    zoo2 = Zoo(100000, "Зоопарк 'ХII місяців'", 230, 1992, "савці")
    zoo3 = Zoo(50000, "Черкаський зоопарк", 200, 2007, "риби")
    zoo4 = Zoo()

    print(zoo1)
    print(zoo2)
    print(zoo3)
    print(zoo4)
    # print(f"тільки кількість: {zoo4.get_vs_number()}")
    print("---------------------------------------------------------------------------------------------")
    print(repr(zoo1))
    print(repr(zoo2))
    print(repr(zoo3))
    print(repr(zoo4))


main()
