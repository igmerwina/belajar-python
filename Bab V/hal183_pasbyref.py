# @igmerwina
# Bab 5 - Pass by Reference
#
# "Tidak ada pass by value dalam python!"

def ubahNilai(params):
    params *= 100
    print "nilai dalam fungsi: ", params
    return

def main():
    a = 5

    print "sebelum fungsi: ", a

    ubahNilai(a)

    print "setelah fungsi: ", a

    # hasilnya sama aja...

if __name__ == "__main__":
    main()
