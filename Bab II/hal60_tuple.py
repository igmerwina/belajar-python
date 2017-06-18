# Bab II hal 60
#   Tuple
# Tuple nilai datanya ndak bisa diubah
# mirip seperti array konstan
# karna ndak bisa diubah, jadi append, insert, extend, tidak berlaku pada tupple
# mau remove juga ndak bisa
# tapi index() masih bisa dipakai
# bisa cek elemen dari tupple menggunakan in
# bukan tupleware

from __future__ import print_function

def main():
    flora = ("Teratai", "Mawar", "Gerbera")

    x = "Teratai" in flora # > hasil dari IDLE = True

    for bunga in flora:
        print(bunga)

if __name__ == "__main__":
    main()
