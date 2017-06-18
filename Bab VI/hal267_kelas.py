# @igmerwina
# Hal 267 contoh Kelas

from __future__ import print_function

class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    def hitungVol(self):
        return self.panjang * self.lebar * self.tinggi

def main():
    # membuat objek Kotak
    kotak1 = Kotak(2, 4, 4)

    # menggunakan objek pertama
    print("Obj kotak I"); print()
    print("Panjang: ", kotak1.panjang)
    print("Lebar:   ", kotak1.lebar)
    print("Tinggi:  ", kotak1.tinggi)
    print("Volume:  ", kotak1.hitungVol())

if __name__ == "__main__":
    main()
