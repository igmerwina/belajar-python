# Bab IV IF - ELSE
# Contoh soal Kartesian
# masih kurang kalau inputannya non int

import sys

def main():
    # bikin inputannya
    x = int(raw_input("Kordinat x:> "))
    y = int(raw_input("Kordinat y:> "))

    # buat definissin di kudran mana
    kuadran = ""

    if x > 0 and y > 0:
        kuadran = "I"
    elif x < 0 and y > 0:
        kuadran = "II"
    elif x < 0 and y < 0:
        kuadran = "III"
    elif x > 0 and y < 0:
        kuadran = "IV"
    else:
        pass

    print "titik x: %d dan y: %d berada pada Kuadran: %s " % (x, y, kuadran)

if __name__ == "__main__":
    main()
