<<<<<<< HEAD
# @ igmerwina
# Bab III, contoh Penggunaan For

def main():
    print "contoh 1:"
    for i in 'Python':
        print i

    # ===========================
    print ""
    print "contoh 2:"

    for subject in ['matematika', 'biologi', 'fisika']:
        print subject

    # ===========================
    print ""
    print "contoh 3: "

    angka = ['satu', 'dua', 'tiga']

    for i in range(len(angka)):
        print "%d. = %s" %(i, angka[i])

    # ===========================
    print ""
    print "contoh 4: "
    # range(ord) --> ngubah ke bilangan bulat dulu...
    for i in range(ord('a'), ord('d')):
        # ...baru ini dikonversi ke huruf dari a ke c
        print chr(i)

if __name__ == "__main__":
    main()
=======
# @ igmerwina
# Bab III, contoh Penggunaan For

def main():
    print "contoh 1:"
    for i in 'Python':
        print i

    # ===========================
    print ""
    print "contoh 2:"

    for subject in ['matematika', 'biologi', 'fisika']:
        print subject

    # ===========================
    print ""
    print "contoh 3: "

    angka = ['satu', 'dua', 'tiga']

    for i in range(len(angka)):
        print "%d. = %s" %(i, angka[i])

    # ===========================
    print ""
    print "contoh 4: "
    # range(ord) --> ngubah ke bilangan bulat dulu...
    for i in range(ord('a'), ord('d')):
        # ...baru ini dikonversi ke huruf dari a ke c
        print chr(i)

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
