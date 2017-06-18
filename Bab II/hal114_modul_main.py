<<<<<<< HEAD
# Bab II Modul
# Ini sambungan dari module_hal_114.py

from __future__ import print_function
import module_hal_114

def main():
    a = 2
    b = 3
    c = 2.5

    # panggil fungsi yang ada di module_hal_114 tadi
    hasiltambah = module_hal_114.tambah(a, b)
    hasilkurang = module_hal_114.kurang(a, b)
    hasilkali = module_hal_114.kali(a, b)
    hasilbagi1 = module_hal_114.bagi(a, b)
    hasilbagi2 = module_hal_114.bagi(a, c)

    # print hasilnya
    print("Hasil tambah: %d + %d = %d" % (a, b, hasiltambah))
    print("Hasil kurang: %d + %d = %d" % (a, b, hasilkurang))
    print("Hasil kali: %d + %d = %d" % (a, b, hasilkali))
    print("Hasil bagi 1: %d + %d = %d" % (a, b, hasilbagi1))
    print("Hasil bagi 2: %d + %d = %d" % (a, b, hasilbagi2))

if __name__ == "__main__":
    main()
=======
# Bab II Modul
# Ini sambungan dari module_hal_114.py

from __future__ import print_function
import module_hal_114

def main():
    a = 2
    b = 3
    c = 2.5

    # panggil fungsi yang ada di module_hal_114 tadi
    hasiltambah = module_hal_114.tambah(a, b)
    hasilkurang = module_hal_114.kurang(a, b)
    hasilkali = module_hal_114.kali(a, b)
    hasilbagi1 = module_hal_114.bagi(a, b)
    hasilbagi2 = module_hal_114.bagi(a, c)

    # print hasilnya
    print("Hasil tambah: %d + %d = %d" % (a, b, hasiltambah))
    print("Hasil kurang: %d + %d = %d" % (a, b, hasilkurang))
    print("Hasil kali: %d + %d = %d" % (a, b, hasilkali))
    print("Hasil bagi 1: %d + %d = %d" % (a, b, hasilbagi1))
    print("Hasil bagi 2: %d + %d = %d" % (a, b, hasilbagi2))

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
