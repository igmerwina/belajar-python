<<<<<<< HEAD
# Bab III
# Contoh Deepcopy

from __future__ import print_function
import copy

def filetolist(filename):
    templist = []
    try:
        f = open(filename)
        for line in f:
            templist.append(line)
    except IOError as e:
        print(e)
        sys.exit(1)
    return templist

def printlist(li):
    for e in li:
        print(e, end='')

def main():
    phonebook = filetolist("data.txt")

    sortedlist = sorted(copy.deepcopy(phonebook))

    print("Sebelum diurutkan: ")
    printlist(phonebook)

    print("\n Setelah diurutkan: ")
    printlist(sortedlist)

if __name__ == "__main__":
    main()
=======
# Bab III
# Contoh Deepcopy

from __future__ import print_function
import copy

def filetolist(filename):
    templist = []
    try:
        f = open(filename)
        for line in f:
            templist.append(line)
    except IOError as e:
        print(e)
        sys.exit(1)
    return templist

def printlist(li):
    for e in li:
        print(e, end='')

def main():
    phonebook = filetolist("data.txt")

    sortedlist = sorted(copy.deepcopy(phonebook))

    print("Sebelum diurutkan: ")
    printlist(phonebook)

    print("\n Setelah diurutkan: ")
    printlist(sortedlist)

if __name__ == "__main__":
    main()
>>>>>>> 9b3f396d94fb204292b94f897479298261a9f32d
