#Bab II contoh Class & objek

from __future__ import print_function

# bikin kelas Node
class Node:
    def __init__(self, element, next = None):
        self.element = element
        self.next = next

# bikin class LinkedList
class LinkedList:
    def __init__(self):
        self.front = None
        self.back = None
        self.size = 0

    def isEmpty(self):
        return self.size == 0

    def addFirst(self, element):
        if self.isEmpty():
            self.front = Node(element)
            self.back = self.front
        else:
            temp = self.front
            self.front = Node(element, temp)
        self.size += 1

    def addLast(self, element):
        if self.isEmpty():
            self.front = Node(element)
            self.back = self.front
        else:
            self.back.next = Node(element)
            self.back = self.back.next
        self.size += 1

    def printList(self):
            print("Isi linked list: ")
            current = self.front
            while current != None:
                print(current.element)
                current = current.next

def main():
    # membuat objek dari kelas LinkedList
    li = LinkedList()

    # menambah elemen di awal
    li.addFirst(10)

    # menambah elemen di akhir
    li.addLast(20)
    li.addLast(30)

    # menambah elemen di awal
    li.addFirst(90)

    # tampil semua nilai node dalam linked list
    li.printList()

if __name__ == "__main__":
    main()
