# Bab II
# menghitung luas dan keliling lingkaran

from __future__ import print_function
import math

def main():
    r = float(raw_input("Masukan jari-jari: >"))

    luas = math.pi * (r ** 2)

    keliling = math.pi * r * 2

    print("====" *4)
    print("Jari-jarinya: ", r)
    print("Luas lingkarannya adalah %2.f" % luas)
    print("Kelilingnya adalah: %2.f" % keliling)

if __name__ == "__main__":
    main()
