<<<<<<< HEAD
# bab II hal 61
# contoh penggunaan tuple

from __future__ import print_function
import datetime as dt # import module datetime untuk tanggalan primbon

def main():
    # karna konstan / ndak bisa diubah, jadi variabel bulan pake huruf kapital
    BULAN = ("Januari", "Februari", "Maret",
             "April", "Mei", "Juni",
             "Juli", "Agustus", "September",
             "Oktober", "November", "Desember")

    #today = YYYY--MM-DD
    # fungsi untuk manggil primbon hari ini
    # isoformat untuk membalik tahun-bulan-tanggal
    today = dt.date.isoformat(dt.date.today())

    yyyy = today[:4] # empat elemen pertama
    mm = today[5:7]  # elemen kelima sampai enam
    dd = today[8:]   # elemen ke delapan

    print(today)
    print("%s %s %s" % (dd, BULAN[int(mm)-1], yyyy))

if __name__ == "__main__":
    main()
=======
# bab II hal 61
# contoh penggunaan tuple

from __future__ import print_function
import datetime as dt # import module datetime untuk tanggalan primbon

def main():
    # karna konstan / ndak bisa diubah, jadi variabel bulan pake huruf kapital
    BULAN = ("Januari", "Februari", "Maret",
             "April", "Mei", "Juni",
             "Juli", "Agustus", "September",
             "Oktober", "November", "Desember")

    #today = YYYY--MM-DD
    # fungsi untuk manggil primbon hari ini
    # isoformat untuk membalik tahun-bulan-tanggal
    today = dt.date.isoformat(dt.date.today())

    yyyy = today[:4] # empat elemen pertama
    mm = today[5:7]  # elemen kelima sampai enam
    dd = today[8:]   # elemen ke delapan

    print(today)
    print("%s %s %s" % (dd, BULAN[int(mm)-1], yyyy))

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
