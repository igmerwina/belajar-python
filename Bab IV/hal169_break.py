# @igmerwina
# Bab III - Contoh Break

from __future__ import print_function

def main():
    for a in range(1,10):
        for b in range(1, 11):
            print(a*b, end='\t')
            if b == 5:
                break
        print()

if __name__ == "__main__":
    main()
