# @igmerwina
# contoh lain metode statis

from __future__ import print_function
import math

class hitung(object):
    def __init__(self, p, l, t):
        pass

    @staticmethod
    def log10(x):
        return math.log10(x)

    @staticmethod
    def log(x):
        return math.log(x)

    @staticmethod
    def kali(x, y):
        return x * y

    @staticmethod
    def pangkat(x, y):
        return math.pow(x, y)

    @staticmethod
    def akar(x):
        return math.sqrt(x)

    @staticmethod
    def absolut(x):
        return abs(x)

def main():
    print("hitung.log10(1000)   = %f " % hitung.log10(1000))
    print("hitung.log(4)        = %f " % hitung.log(4))
    print("hitung.kali(2, 4)    = %f " % hitung.kali(2,4))
    print("hitung.pangkat(2, 6) = %f " % hitung.pangkat(2,6))
    print("hitung.akar(81)      = %f " % hitung.akar(81))
    print("hitung.absolut(-9)   = %f " % hitung.absolut(-9))

if __name__ == '__main__':
    main()
