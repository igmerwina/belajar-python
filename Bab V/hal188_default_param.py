<<<<<<< HEAD
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
=======
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
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
