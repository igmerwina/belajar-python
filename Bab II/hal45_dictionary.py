# hal 45
# Tipe dictonary

from __future__ import print_function

def main():
    d = {'satu': 10, 'dua': 20, 'tiga': 30}

    print("d[satu]: ", d['satu'])
    print("d[dua]: ", d['dua'])
    print("d[tiga]: ", d['tiga'])

    print("d[satu] * d[dua] => ", d['satu'], "*", d['dua'], "=", d['satu'] * d['dua'] )

    # cara lain
    print("\n","=" *10)
    print("d[satu]: " +str(d['satu']))

    print("d[satu] * d[dua] = " +str(d['satu'] * d['dua']))

if __name__ == "__main__":
    main()
