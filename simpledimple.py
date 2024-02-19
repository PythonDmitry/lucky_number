from math import sqrt


def simpledimple(number):
    b = False
    count = int(sqrt(number))
    while count > 1:
        if number % count == 0:
            b = True
        count -= 1
    return b

for nummm in range(2, 100):
    if not simpledimple(nummm):
        print(nummm)
