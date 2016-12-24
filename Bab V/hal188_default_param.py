# @igmerwina
# Bab 5 contoh default parameter pada list

from __future__ import print_function

def cetakDaftar(alist=[], urut = False):
    if urut:
        alist.sort()
    for i in alist:
        print(i, end = ' ')
    print()
    return

def main():
    # bikin list
    li = [65,34, 55, 100, 88]

    print("Unsorted: ")
    cetakDaftar(li)

    print("Sorted: ")
    cetakDaftar(li, True)

if __name__ == "__main__":
    main()
