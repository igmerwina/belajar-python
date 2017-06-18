# @igmerwina
# hal 282 meotde kelas

from __future__ import print_function

class tanggal(object):
    def __init__(self, dd = 0, mm = 0, yyyy = 0):
        self.hari = tanggal.hari = dd
        self.bulan = tanggal.bulan = mm
        self.tahun = tanggal.tahun = yyyy

    @classmethod
    def dariString(cls, strTanggal):
        hari, bulan, tahun = map(int, strTanggal.split('-'))
        objekTanggal = cls(hari, bulan, tahun)
        return objekTanggal

    def cetakTanggal(self):
        BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni"
                 "Juli", "Agustus", "September", "Oktober", "Nopember", "Desember"]
        print("%d %s %d" %(self.hari, BULAN[self.bulan-1], self.tahun))

def main():
    # membuat objek dari class tanggal
    # dengan cara yang umum
    obj1 = tanggal(28, 10, 1992)

    # membuat objek dari class tanggal
    # pakai metode class
    obj2 = tanggal.dariString("13-10-1998")

    # cetak tanggal
    print("Tanggal pada obj1: ", end=' ')
    obj1.cetakTanggal()
    print("Tanggal pada obj1: ", end=' ')
    obj2.cetakTanggal()

if __name__ == '__main__':
    main()
