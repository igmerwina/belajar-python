<<<<<<< HEAD
# Latihan Bab II Faktorial

from __future__ import print_function
import sys

def main():
    n = int(raw_input("faktorial berapa?:> "))

    # input ndak boleh minus
    if n < 0: print("ndak boleh minus oy!"); sys.exit(1)

    print("%d faktorial: " %n)

    # niali awal faktorial pasti 1
    fak = 1

    # lakukan perulangan sampek bosan
    while n >= 1:
        # perhitungannya di sini
        # jadi 1 * (n-1) * (n-1) * (n-1)
        fak = fak * n
        n = n - 1

    print("hasilnya: ", fak)

if __name__ == "__main__":
    main()
=======
# Latihan Bab II Faktorial

from __future__ import print_function
import sys

def main():
    n = int(raw_input("faktorial berapa?:> "))

    # input ndak boleh minus
    if n < 0: print("ndak boleh minus oy!"); sys.exit(1)

    print("%d faktorial: " %n)

    # niali awal faktorial pasti 1
    fak = 1

    # lakukan perulangan sampek bosan
    while n >= 1:
        # perhitungannya di sini
        # jadi 1 * (n-1) * (n-1) * (n-1)
        fak = fak * n
        n = n - 1

    print("hasilnya: ", fak)

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
