# @igmerwina
# hal 279 method statis

from __future__ import print_function

class Kotak(object):
    ObjectCounter = 0

    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t
        # setiap objek dibuat objek ocunter dinaikkan 1
        Kotak.ObjectCounter += 1

    def hitungVol(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("==" * 10)
        print("Panjang: ", self.panjang)
        print("Lebar  : ", self.lebar)
        print("Tinggi : ", self.tinggi)

    def cetakVol(self):
        print("Volume = ", self.hitungVol())
        print()

    @staticmethod
    def cetakJudul():
        if Kotak.ObjectCounter > 1:
            print()
        print("Objek kotak ke: ", Kotak.ObjectCounter)

def main():
    # membuat objek pertama
    kotak1 = Kotak(6, 2, 3)

    # cara panggilnya : Class.staticmethod
    Kotak.cetakJudul()
    kotak1.cetakData()
    kotak1.cetakVol()

    kotak2 = Kotak(5, 2, 6)
    Kotak.cetakJudul()
    kotak2.cetakData()
    kotak2.cetakVol()

    kotak3 = Kotak(9, 2, 6)
    Kotak.cetakJudul()
    kotak3.cetakData()
    kotak3.cetakVol()

if __name__ == "__main__":
    main()
