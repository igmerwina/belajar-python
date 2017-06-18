# @igmerwina
# hal 273 - contoh destruktor untuk nutup file
# masih error!!!

from __future__ import print_function

class MyFile(object):
    def __init__(self, namafile):
        self.file = open(namafile)

    def __del__(self):
        self.file.close()

    def bacadata(self):
        for baris in self.file:
            print(baris, end="")

def main():
    # membuat objek dari kelas my file
    """ kok eror ya ini lokasi filenya hmmm """

    f = MyFile("D:\\kodepython\\sample.txt")

    # memanggil metode bacadata()
    f.bacadata()

if __name__ == "__main__":
    main()
