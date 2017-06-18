# Bab II
# latian konvert farenheit ke celcius

from __future__ import print_function

def main():
    f = float(raw_input("suhu dalam farenheit:> "))

    c = (5 * (f - 32)) / 9

    print("suhu sama dengan %d celcius" % c)

if __name__ == "__main__":
    main()
