import math


def trojkat(a: int, b: int):
    try:
        c = math.sqrt(a ** 2 + b ** 2)
        return c

    except TypeError:
        raise TypeError('Nie wpisałeś liczby. Podaj ponownie długość boku trójkąta.')


print(trojkat(2, 4))
