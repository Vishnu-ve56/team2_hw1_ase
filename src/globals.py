import math
def rnd(n, places):
    mult=10**(places or 3)
    return math.floor(n*mult + 0.5)/mult
