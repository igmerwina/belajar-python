# Bab II Modul
# File modul ini berhubungan dengan II 114_modul_main.py

def tambah(a, b):
    return a + b

def kurang(a, b):
    return a - b

def kali(a, b):
    return a * b

def bagi(a,b):
    if isinstance(a, int) and isinstance(b, int):
        return a//b
    else:
        return a/b
