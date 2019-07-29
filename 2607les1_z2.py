class Shop:
    # _name = None
    # _countware = None
    # _sum_countware = None
    def __init__(self, n, c):
        self.name = n
        self.countware = c

shop1 = Shop("ASHAN", 100)
shop2 = Shop("Bila", 200)
shop3 = Shop("ATB", 300)
total = shop1.countware + shop2.countware + shop3.countware
print("Всего по магазинам продано - ")
print(total)

    # def set_name(self, name):
    #     self.name = name
    # def __get__(self, instance, owner):t_name()


