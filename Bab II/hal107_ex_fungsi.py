# Bab II Contoh Penggunaan fungsi

from __future__ import print_function
import datetime as dt

def getisoformat(date):
    return dt.date.isoformat(date)

def day(date):
    datestr = getisoformat(date)
    return int(datestr[8:])

def month(date):
    datestr = getisoformat(date)
    return int(datestr[5:7])

def year(date):
    datestr = getisoformat(date)
    return int(datestr[:4])

def main():
    today = dt.date.today()
    print(getisoformat(today))
    print("Hari\t: %d" % day(today))
    print("Bulan\t: %d" % month(today))
    print("Tahun\t: %d" % year(today))

if __name__ == "__main__":
    main()
