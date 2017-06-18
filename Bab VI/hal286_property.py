# @igmerwina
# hal 286 - Property

from __future__ import print_function

class Titik(object):
    def __init__(self, x=None, y=None):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, nilai):
        if (not isinstance(nilai, int)) and \
           (not isinstance(nilai, float)):
           raise TypeError("x harus bertipe numerik")
        self.__x = nilai

    @x.deleter
    def x(self):
        # menghappus self.__x dari memori
        del self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, nilai):
        if (not isinstance(nilai, int)) and \
           (not isinstance(nilai, float)):
           raise TypeError("y harus bertipe numerik")
        self.__y = nilai

    @y.deleter
    def y(self):
        # menghappus self.__y dari memori
        del self.__y

def main():
    # membuat objek dari kelas Titik
    A = Titik()
    B = Titik(2, 5)

    # menentukan nilai __x dan __y di dalam A
    # melalui properti x & y
    A.x = 4
    A.y = 2

    # mengambil nilai __x dan __y di dalam A
    # melalui property x & y
    print("A(%d, %d)" %(A.x, A.y))

    # mengambil nilai __x dan __y di dalam B
    # melalui property x & y
    print("B(%d, %d)" %(B.x, B.y))

if __name__ == '__main__':
    main()
