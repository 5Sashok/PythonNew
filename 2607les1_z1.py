class Automobil:
    _seats = 4
    _wheels = 4
    _fuel = "diesel"
    _electro = False

    def get_seats(self):
        return self._seats
    def get_wheels(self):
        return self._wheels
    def get_fuel(self):
        return self._fuel
    def get_electro(self):
        return self._electro


def SportCar():
    pass


class SportCar(Automobil):
    _seats = 2
    _wheels = 4
    _fuel = "gas"
    auto = Automobil()
sportcar = SportCar()
print(sportcar.get_seats())


class Truck(object):
    pass


# noinspection PyRedeclaration
class Truck(Automobil):
    _seats = 2
    _wheels = 6
    _fuel = "diesel"

truck=Truck()
print(truck.get_fuel())






