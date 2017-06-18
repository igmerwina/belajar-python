<<<<<<< HEAD
# Bab III, contoh xrange

from __future__ import print_function

# ini buat print hasilnya (genap / ganjil)
def printlist(li):
    for e in li:
        print(e, end=' ')
    print

def main():
    bilangan = xrange(20) # 1 sampai 19
    genap = []
    ganjil = []

    for x in bilangan:
        if x % 2 == 0:
            # x ditambahin ke genap pakai fungsi append
            genap.append(x)
        else:
            # x ditambahin ke ganjil pakai fungsi append
            ganjil.append(x)

    print("Bilangan genap:\t ", end='')
    printlist(genap)

    print()

    print("Bilangan ganjil: ", end='')
    printlist(ganjil)

if __name__ == "__main__":
    main()
=======
# Bab III, contoh xrange

from __future__ import print_function

# ini buat print hasilnya (genap / ganjil)
def printlist(li):
    for e in li:
        print(e, end=' ')
    print

def main():
    bilangan = xrange(20) # 1 sampai 19
    genap = []
    ganjil = []

    for x in bilangan:
        if x % 2 == 0:
            # x ditambahin ke genap pakai fungsi append
            genap.append(x)
        else:
            # x ditambahin ke ganjil pakai fungsi append
            ganjil.append(x)

    print("Bilangan genap:\t ", end='')
    printlist(genap)

    print()

    print("Bilangan ganjil: ", end='')
    printlist(ganjil)

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
