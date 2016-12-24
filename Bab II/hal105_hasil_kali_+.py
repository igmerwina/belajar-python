# Bab II latihan operator kali dengan plus
# 3 * 3 = 3 + 3 + 3 = 9

from __future__ import print_function

def main():
    a = int(raw_input("> "))
    b = int(raw_input("> "))

    hasil = 0
    for i in range(0, b):
        hasil = hasil + a

    print(hasil)

if __name__ == "__main__":
    main()
