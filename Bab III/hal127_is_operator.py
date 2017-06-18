# Bab III, Contoh penggunaan operator is dan ==

from __future__ import print_function

class Kotak:
    def __init__(self, p, l, t):
        self.p = p
        self.l = l
        self.t = t

    def equals(self, obj):
        if self.p == obj.p and self.l == obj.l and self.t == obj.t:
           return True
        else:
            return False

    def isreferencedby(self, ref):
        if ref is self:
            return True
        else:
            return False

def main():
    k1 = Kotak(6,5,3)
    k2 = Kotak(6,5,3)
    k3 = k1

    print("k1.equals(k2)\t\t: " + str(k1.equals(k2)))
    print("k1.isreferencedby(k2)\t: " + str(k1.isreferencedby(k2)))
    print()
    print("k1.equals(k3)\t\t: " + str(k1.equals(k3)))
    print("k1.isreferencedby(k3)\t: " + str(k1.isreferencedby(k3)))

if __name__ == "__main__":
    main()
