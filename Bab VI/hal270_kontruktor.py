# @igmerwina
# hal 270 contoh overload pada konstruktor

from __future__ import print_function

class Kotak(object):
    def __init__(self, p=0, l=0, t=0):
        self.panjang = p
        self.lebar   = l
        self.tinggi  = t

    def setData(self, p, l, t):
        self.panjang = p
        self.lebar   = l
        self.tinggi  = t

    def hitungVol(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("==" * 10)
        print("Panjang: ", self.panjang)
        print("Lebar  : ", self.lebar)
        print("Tinggi : ", self.tinggi)

    def cetakVol(self):
        print()
        print("Volume = ", self.hitungVol())

def main():
    # membuat objek pertama dengan construct tanpa parameter
    kotak1 = Kotak()
    kotak1.setData(4, 2, 5)
    print("Objek I")
    kotak1.cetakData()
    kotak1.cetakVol()

    # objek kedua dengan parameter
    kotak2 = Kotak(1, 4, 5)
    print(); print("Objek II")
    kotak2.cetakData()
    kotak2.cetakVol()

if __name__ == "__main__":
    main()
