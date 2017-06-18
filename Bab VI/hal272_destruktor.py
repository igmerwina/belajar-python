# @igmerwina
# hal 272 contoh destruktor

from __future__ import print_function

class Kotak(object):
    def __init__(self, p, l, t):
        print("Konstruktor kotak dipanggil")
        self.panjang = p
        self.lebar   = l
        self.tinggi  = t

    def __del__(self):
        print("Destruktor dipanggil")

    def hitungVol(self):
        return self.panjang * self.lebar * self.tinggi

    def cetakData(self):
        print("==" * 10)
        print("Panjang: ", self.panjang)
        print("Lebar  : ", self.lebar)
        print("Tinggi : ", self.tinggi)

    def cetakVol(self):
        print("Volume = ", self.hitungVol())
        print("==" * 10)

def main():
    # membuat objek
    kotak = Kotak(2, 4, 6)

    # menggunakan objek
    kotak.cetakData()
    kotak.cetakVol()

    # menghapus objek manualy
    # menggunakan Destruktor
    del kotak

if __name__ == "__main__":
    main()
