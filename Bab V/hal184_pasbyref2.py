# @igmerwina
# Bab 5 - Pass by Reference 2

def ubahNilai(params):
    params *= 100
    print "== di dalam fungsi =="
    print "nilai params dalam fungsi: ", params
    print "id params dalam fungsi: ", id(params)
    print ""
    return

def main():
    a = 5

    print "sebelum fungsi: ", a
    print "id a ", id(a)
    print ""

    ubahNilai(a)

    print "setelah fungsi: ", a
    print "id a ", id(a)

    # hasilnya sama aja...

if __name__ == "__main__":
    main()
