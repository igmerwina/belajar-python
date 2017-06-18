<<<<<<< HEAD
# @igmerwina
# Bab 5 - COntoh Fungsi

from __future__ import print_function
import os

# tanpa return
def printNonline(text):
    "Print text tanpa return"
    print(text, end='')

# dengan return
def tambah(angka):
    return angka **2

def cls():
    "Clear screen"
    os.system("cls")

def main():

    printNonline("Umur = ") # parameter bisa langsung isi string
    printNonline(20)

    # panggil fungsi tambah
    a = tambah(88); print(a)

if __name__ == "__main__":
    main()
=======
# @igmerwina
# Bab 5 - COntoh Fungsi

from __future__ import print_function
import os

# tanpa return
def printNonline(text):
    "Print text tanpa return"
    print(text, end='')

# dengan return
def tambah(angka):
    return angka **2

def cls():
    "Clear screen"
    os.system("cls")

def main():

    printNonline("Umur = ") # parameter bisa langsung isi string
    printNonline(20)

    # panggil fungsi tambah
    a = tambah(88); print(a)

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
