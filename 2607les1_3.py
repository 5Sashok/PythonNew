class Automobile:

    _seats = 4
    _wheels = 4
    _engine = "V8"
    _electro = False

    def set_seats(self, seats):
        self.seats = seats
    def get_seats(self):
        return self._seats
    def get_wheels(self):
        return self._wheels
    def get_engine(self):
        return self._engine
    def get_electro(self):
        return self._electro

class Bus(Automobile):
    _seats = 40
    _wheels = 6

    # def __add__(self, other):
    #     result = self.get_seats() + other.get_seats()
    #     return result
    def beep(self):
        print("BEEP-BEEP!")
auto = Automobile()
print(auto.__class__)
print(auto.get_seats())
print(auto.get_wheels())
bus = Bus()
print(bus.__class__)
print(bus.get_seats())
print(bus.get_wheels())
print(bus.get_electro())
print(bus.get_engine())
bus.beep()

# car = Automobile()
#
# car.set_seats(8)
# print(car.get_seats())
#
# #print(Automobile._seats())
print(auto + bus)