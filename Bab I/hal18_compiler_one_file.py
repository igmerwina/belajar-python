# @ igmerwina
# Bab I
# COntoh compiler untuk python

#!Python27\python

from __future__ import print_function
import os, py_compile

def main():
    os.chdir("F:\\python")
    py_compile.compile("hello.py")
    print("File hasil compile telah dibuat..")
    os.system("pause");

if __name__ == "__main__":
    main()
