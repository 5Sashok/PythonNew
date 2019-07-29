class Vehicle ():
    _x = None

    def set_x(self,x):
        self._x = x

    def get_x(self):
        return self._x

    def del_x(self):
        del self._x

    x = property(get_x, set_x, del_x, "I'm the 'x' property.")

xz = Vehicle()
xz.x = 5
print( xz.x )