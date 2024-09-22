class House:

    houses_history = []

    def __new__(cls, *args):

        name = args[0]
        cls.houses_history.append(name)
        instance = super().__new__(cls)
        instance.__init__(name, args[1])
        return instance


    def __init__(self, name, number_of_floors):

        self.name = name
        self.number_of_floors = number_of_floors
        House.houses_history.append(name)



    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __del__(self):
        print(f"{self.name} снесён, но он останется в истории")





h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)


del h2
del h3

print(House.houses_history)