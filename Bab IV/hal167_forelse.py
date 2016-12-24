# @igmerwina
# Bab III - Penggunaan Else dalam Loop

from __future__ import print_function

def main():
    # print 10 - 25
    for i in range(10, 25):

        # 2 sampai i;
        # maksudnya 2 sampai 10
        # terus 2 sampai 11
        # dst sampai 24
        for j in range(2, i):
            if i % j == 0:
                print("%d bukan prima" % i)
                # stop kalau emang i % j = 0
                break
            else:
                print("%d prima" % i)
                break

if __name__ == "__main__":
    main()
