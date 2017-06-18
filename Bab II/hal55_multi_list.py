# bab II hal 55
# buat list mirip kaya array multi dimensi

from __future__ import print_function

def main():
    #el: 0  1  ------- 2 --------
    d = [1, 2, ["ayam", "bebek"]]

    print(d[1])
    print(d[2])
    print(d[2][0]) #prin elemen ke dua yang ke nol, paham? yes!

if __name__ == "__main__":
    main()
