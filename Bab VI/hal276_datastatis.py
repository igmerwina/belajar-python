# @igmerwina
# hal 276 data statis
# variable class & variable objek

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

def main():
    # membuat objek pertama
    kotak1 = Kotak(6, 2, 3)
    print("Ini objek ke: ", kotak1.ObjectCounter)
    kotak1.cetakData()
    kotak1.cetakVol()

    kotak2 = Kotak(5, 2, 6)
    print("Ini objek ke: ", kotak2.ObjectCounter)
    kotak2.cetakData()
    kotak2.cetakVol()

    kotak3 = Kotak(9, 2, 6)
    print("Ini objek ke: ", kotak3.ObjectCounter)
    kotak3.cetakData()
    kotak3.cetakVol()

    # memanggil object counter
    print("Objek counter pada objek I: ", kotak1.ObjectCounter)
    print("Objek counter pada objek II: ", kotak2.ObjectCounter)
    print("Objek counter pada objek III: ", kotak3.ObjectCounter)

if __name__ == "__main__":
    main()
