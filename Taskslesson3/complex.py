class Complex:
    def __init__(self, *args):
        print(self)
x = Complex
x = complex(4, 5)
print(x)
y = Complex
y = complex(3, 7)
print(y)
#     Комплексные числа можно складывать, вычитать, умножать, делить и возводить в степень.
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x ** y)
print(x ** 2)

