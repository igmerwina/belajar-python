<<<<<<< HEAD
# @igmerwina
# Bab III If Else
# Menggunakan if else pada dictionary 2

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def main():
    a = float(raw_input("Masukan nila a:> "))
    b = float(raw_input("Masukan nila b:> "))
    op = raw_input("Operatornya?> ")

    d = {
        '+': tambah(a,b),
        '-': kurang(a,b),
        '*': kali(a,b),
        '/': bagi(a,b),
    }

    # d[op] --> d yang isinya operator inputan
    # uh.. oooh..

    print "a: %.2f %s b: %.2f = %.2f " % (a, op, b, d[op])

if __name__ == "__main__":
    main()
=======
# @igmerwina
# Bab III If Else
# Menggunakan if else pada dictionary 2

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a, b):
    return a / b

def main():
    a = float(raw_input("Masukan nila a:> "))
    b = float(raw_input("Masukan nila b:> "))
    op = raw_input("Operatornya?> ")

    d = {
        '+': tambah(a,b),
        '-': kurang(a,b),
        '*': kali(a,b),
        '/': bagi(a,b),
    }

    # d[op] --> d yang isinya operator inputan
    # uh.. oooh..

    print "a: %.2f %s b: %.2f = %.2f " % (a, op, b, d[op])

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
