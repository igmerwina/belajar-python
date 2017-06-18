# @igmerwina
# hal 268 contoh metode

from __future__ import print_function

class Kotak(object):
    def __init__(self, p, l, t):
        self.panjang = p
        self.lebar = l
        self.tinggi = t

    # self ini = parameter wajib dalam tiap class / method
    def hitungVol(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("Panjang: ", self.panjang)
        print("Lebar:   ", self.lebar)
        print("Tinggi:  ", self.tinggi)

    def cetakVol(self):
        print("Volume:  ", self.hitungVol())

def main():
    print("Obj kotak I"); print()

    # membuat objek Kotak
    kotak1 = Kotak(2, 4, 4)
    # panggil meotode dari objek
    kotak1.cetakData()
    kotak1.cetakVol()

    print(); print("Obj kotak II"); print()

    # membuat objek Kotak
    kotak1 = Kotak(2, 6, 8)
    # panggil meotode dari objek
    kotak1.cetakData()
    kotak1.cetakVol()
if __name__ == "__main__":
    main()
