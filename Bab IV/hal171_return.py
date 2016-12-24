# @igmerwina
# Bab III - Contoh Return

from __future__ import print_function

def tambah(a, b):
    c = a + b
    # nilai harus dikasi liat (dikembaliin)
    return c

def main():
    x = int(raw_input("x> "))
    y = int(raw_input("y> "))

    hasil = tambah(x, y)

    print("%d + %d = %d" %(x, y, hasil))

if __name__ == "__main__":
    main()
