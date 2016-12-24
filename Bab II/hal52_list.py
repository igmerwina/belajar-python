# Bab II hal 52
# List
# bedanya sama dictionary, kalau list ndak ada key nya

from __future__ import print_function

def main():
    li = [10, 20, 30]

    # print biasa
    print("cara biasa", "\n", "=" *10)
    print(li[0], "\n")

    # pakai for
    print("pake for\n", "=" *10,)
    for i in li:
        print(i)

    # pakai elemen minus [-]
    print("\npake elemen minus\n", "=" *10)
    print(li[-1])


if __name__ == "__main__":
    main()
