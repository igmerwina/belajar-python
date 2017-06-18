<<<<<<< HEAD
""" Bab II: Set & frozenset
digunakan untuk membuat himpunan
tidak ada elemen yang sama, kalau ada akan dihapus otomatis

tambah elemen pakai add/update
hapus pakai remove
kosongin elmen pakai clear()

=============================================
kalau mau himpunan yang elemennya bener2 ndak bisa diubah,
bisa pakai frozenset([])
 """

from __future__ import print_function
import sys

def printElement(s, info):
    print(info)
    if len(s) == 0:
        print("Himpunan Kosong\n")
        sys.exit(1)
    for e in s:
        print(str(e) + " ", end='')
    print("\n")

def main():
    # bikin Himpunan
    s  = set([1,2,3,4])

    printElement(s, "Elemen Awal: ")

    #tambah anggota ke elemen baru
    s.add(5);
    s.update([6]);
    printElement(s, "After add: ")

    # hapus elemen
    s.remove(1)
    printElement(s, "Setelah hapus")

    # truncate
    print("setelah clear: ")
    s.clear()
    printElement(s, "Habis deh")

if __name__ == "__main__":
    main()
=======
""" Bab II: Set & frozenset
digunakan untuk membuat himpunan
tidak ada elemen yang sama, kalau ada akan dihapus otomatis

tambah elemen pakai add/update
hapus pakai remove
kosongin elmen pakai clear()

=============================================
kalau mau himpunan yang elemennya bener2 ndak bisa diubah,
bisa pakai frozenset([])
 """

from __future__ import print_function
import sys

def printElement(s, info):
    print(info)
    if len(s) == 0:
        print("Himpunan Kosong\n")
        sys.exit(1)
    for e in s:
        print(str(e) + " ", end='')
    print("\n")

def main():
    # bikin Himpunan
    s  = set([1,2,3,4])

    printElement(s, "Elemen Awal: ")

    #tambah anggota ke elemen baru
    s.add(5);
    s.update([6]);
    printElement(s, "After add: ")

    # hapus elemen
    s.remove(1)
    printElement(s, "Setelah hapus")

    # truncate
    print("setelah clear: ")
    s.clear()
    printElement(s, "Habis deh")

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
