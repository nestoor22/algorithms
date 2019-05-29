from doubleLinked import *

if __name__ == '__main__':

    while True:
        A = DoublyLinkedList()
        print("'a' - додати елемент в кінець списку\n'p' - додати елемент в початок списку,\n"
              "'m' - додати елемент за позицією\n'r' - видалити перший елемент\n'd' - видалити останній елемент\n"
              "'b' - видалити елемент за позицією\n'j' - видалити елемент за значенням\n"
              "'s' - вивести список\n'e' - вийти\n")
        while True:
            i = input()
            if i == 'a':
                elem = input("Вкажіть елемент: ")
                A.append(elem)
                A.show(A.head)
            elif i == 'p':
                elem = input("Вкажіть елемент: ")
                A.push(elem)
                A.show(A.head)
            elif i == 'd':
                A.del_end()
                A.show(A.head)
            elif i == 'r':
                A.del_beg()
                A.show(A.head)
            elif i == 'm':
                pos = int(input("Вкажіть позицію: "))
                el = input("Вкажіть елемент: ")
                A.add_mid(pos, el)
                A.show(A.head)

            elif i == 's':
                A.show(A.head)
            elif i == 'b':
                pos = int(input("Вкажіть позицію: "))
                A.del_pos(pos)
                A.show(A.head)
            elif i == 'j':
                el = input("Вкажіть елемент: ")
                A.del_elem(el)
                A.show(A.head)
            else:
                break
