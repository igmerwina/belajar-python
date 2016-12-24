# bab II hal 58
# mengahpuse elemen dari list

from __future__ import print_function

def main():
    hewan = ["cicak", "tokek", "sapi"]

    # print awal:
    print("Elemen awal:")
    print(hewan)

    # elemen yang dihapus
    hewan.remove("cicak") #cuma bisa isi satu parameter makananya: remove("satu parameter")
    print("\n", "Setelah dihapus")
    print(hewan)

if __name__ == "__main__":
    main()
