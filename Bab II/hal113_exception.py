# Bab II Exception
# Exception ini maksudnya custom error yang kita bikin sendiri

from __future__ import print_function
import sys

def main():
    try:
        filename = "contoh.txt"

        # membuka file
        f = open(filename)  #munkin akan muncul IOError

        # buka file contoh.txt
        for line in f:
            print(line, end='')

        #nutup file
        f.close()

    except IOError as e:
        print("file '%s' tidak ditemukan" % filename)
        sys.exit()

if __name__ == "__main__":
    main()
