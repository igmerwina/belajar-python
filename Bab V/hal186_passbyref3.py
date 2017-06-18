<<<<<<< HEAD
# @igmerwina
# Bab 5 - Pass by Reference 3
#
# Nilai akan berubah setelah pemanggilan fungsi

def ubahNilai(params):
    params[0] *= 100
    print "== di dalam fungsi =="
    print "nilai params[0]: ", params[0]
    print ""
    return

def main():
    li = [4]

    print "sebelum fungsi: "
    print "li[0] = ", li[0]
    print ""

    ubahNilai(li)

    print "setelah fungsi: "
    print "li[0] = ", li[0]

if __name__ == "__main__":
    main()
=======
# @igmerwina
# Bab 5 - Pass by Reference 3
#
# Nilai akan berubah setelah pemanggilan fungsi

def ubahNilai(params):
    params[0] *= 100
    print "== di dalam fungsi =="
    print "nilai params[0]: ", params[0]
    print ""
    return

def main():
    li = [4]

    print "sebelum fungsi: "
    print "li[0] = ", li[0]
    print ""

    ubahNilai(li)

    print "setelah fungsi: "
    print "li[0] = ", li[0]

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
