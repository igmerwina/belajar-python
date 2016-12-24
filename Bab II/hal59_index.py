# bab II hal 59
# mencari elemen dalam list
# index hanya punya 1 parameter

from __future__ import print_function

def main():
    buah = ["pepaya", "Timun", "Jeruk"]
    print(buah)

    # mencari elemennya
    print("\n Jeruk ada pada index ke", buah.index("Jeruk"))
    print("\n Timun ada pada index ke", buah.index("Timun"))
    
if __name__ == "__main__":
    main()
