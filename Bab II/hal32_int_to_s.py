# hal 32 pyhton buku budi raharjo
# integer to string convention

from __future__ import print_function

def main():
    s = raw_input("Bilangan bulat:> ")

    bil_bulat = int(s)

    hasil = bil_bulat + 1

    print("Bilangan yang dimasukkan adalah: %d" % bil_bulat)
    print("%d + 1 = %d" % (bil_bulat, hasil))

if __name__ == "__main__":
    main()
