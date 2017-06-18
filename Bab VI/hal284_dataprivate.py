# @igmerwina
# hal 284 data private

from __future__ import print_function

class Titik(object):
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    # setter
    def setx(self, x):
        self.__x = x

    def sety(self, y):
        self.__y = y

    # getter
    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

def main():
    # membuat objek dari kelas Titik
    A = Titik()

    # menentukan nilai x & y di dalam A
    A.setx(3)
    A.sety(5)

    # ambil nilai dalam A
    print("A(%d, %d)" % (A.getx(), A.gety()))

if __name__ == '__main__':
    main()
