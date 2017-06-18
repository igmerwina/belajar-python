# @igmerwina
# Bab III - Contoh Nested Loop

from __future__ import print_function

def main():

    # === cara pertama (pakai while): ===

    i = 1
    # kalau i <= 10 aja:
    # artinya kan 1 nambah terus sampai 10
    # kunci tambahnya dia i += 1
    while i <= 10:
        j = 1
        # kalau yang ini barti i nya bisa 1 2 3 --- 10
        # j <= i barti perkalian yang sama ndak diitung
        # makanya hasilnya segitiga bermuda
        while j <= i:
            # (i*j) --> 1*1, 1*2 dst..
            print("%d" %(i*j), end=' ')
            j += 1
        print()
        i += 1

    print()
    print("===" *10, "\n")

    # === cara kedua (pakai for): ===

    # print a = 1 - 10
    for a in range(1, 11):
        # print(a, end =' ')
        # 1 diprin 10 kali, terus a+1 atau 1+1, kemudian 2+1
        for b in range(1, a+1):
            print("%d" %(a * b), end=' ')
        print()

    # === cara ketiga (pakai while dan for): ===
    print()
    print("===" *10, "\n")

    x = 1
    while x <= 10:
        # y nambah satu terus sampai 10
        for y in range(1, x + 1):
            print("%d" %(x * y), end=' ')
        print()
        # x nambah satu terus sampai 10
        x += 1

if __name__ == "__main__":
    main()
