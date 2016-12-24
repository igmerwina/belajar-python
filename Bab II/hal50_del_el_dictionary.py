# Bab II hal 50
# Menghapus elemen dari dictionary

from __future__ import print_function

def main():
    d = {'satu': 10, 'dua':"kampret", 'tiga': "sapi"}

    print("ini sebelum dihapus")
    print(d)

    del d['satu']
    print("after")
    print(d)

if __name__ == "__main__":
    main()
