# Задача № 1
def raschet_znacheniya(z):
    if z < 10:
        def raschet_1(x,y):
            return x**y
        return raschet_1
    elif 10 < z < 20:
        def raschet_2(x,y):
            return x/y
        return raschet_2
    else:
        def raschet_3(x,y):
            return x*y
    return raschet_3

result_1 = raschet_znacheniya(z=3)
print(result_1(4, 5))

result_2 = raschet_znacheniya(z=15)
print(result_2(20, 4))

result_3 = raschet_znacheniya(z=25)
print(result_3(8, 9))

# Задача № 2
znacheniye_1 = lambda x, y, z: (x*y)**z
print(znacheniye_1(2, 3, 4))

def znacheniye_2(x, y, z):
    return (x*y)**z
resultat = znacheniye_2(5, 6, 2)
print(resultat)

#Задача № 3
class Rect:

    def __init__(self, a):
        self.a = a

    def __call__(self, b):
        return self.a * b

pryamougolnik = Rect(3)
ploshad = pryamougolnik(6)
print('Стороны прямоугольника: 3 и 6 см')
print(f'Площадь прямоугольника: {ploshad} кв. см')








