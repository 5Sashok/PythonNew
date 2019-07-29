class Animal:

    animal_type = None
    name = None
    animals_created = 0

    @classmethod
    def get_class_var(cls):
        pass
    def __init__(self, name, animal_type):
        self.name = name
        self.animal_type = animal_type
        Animal.animals_created += 1
    # def __del__(self):
    #     print("Instance is deleted from memory :(")
    def move(self):
        print("i`m moving")
    def eat(self):
        print("i`m eating")
    def sleep(self):
        print("i`m sleeping")
    def who_am_i(self):
        print("I`m the {0}. My type is {1}".format(self.name, self.animal_type))

animal_object = Animal("Human", "Mammal")
animal_object1 = Animal("Human", "Mammal")
print(Animal.animals_created)
# animal_object.name = "Human"
# animal_object.animal_type = "Mammal"
# animal_object.eat()
# animal_object.move()
# animal_object.sleep()
# animal_object.who_am_i()
# print(Animal.name)
#
# del animal_object

