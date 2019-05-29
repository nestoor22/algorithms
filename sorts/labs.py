from sort import *

if __name__ == '__main__':
    A = [2, 0, 4, 1, 5, 3, 6, 7, 8, 9]
    B = [1, 4, 2, 0, 5, 8, 7, 6, ]
    C = [9, 1, 2, 0, 4, 3, 8, 6, 5, 7]
    # D = [4, 1, 3, 2, 5, 9, 6, 7, 0, 1, 1]
    # E = [43, 8, 2, 74, 23, 5, 0, 1, 9, 4]
    # G = [5, 3, 12, 6, 3, 9, 0, 4, 2]
    # F = [6, 7, 1, 43, 21, 35, 15, 6, 5, 0]
    # H = [4, 6, 2, 1, 7, 11, 54, 12, 2, 0]

    # while True:
    #     element = str(input("Enter elements: "))
    #     if element != '':
    #         alist.append(int(element))
    #     else:
    #         print("List: ", alist)
    #         break
    print("1 - Bubble sort\n2 - Selection sort\n3 - Insertion sort\n4 - Exit")
    while True:
        try:
            choice = int(input())
        except ValueError:
            print("Enter correct value")
            continue
        if choice == 1:
            print("List:  ", A)
            print('Result:', bubble_sort(A))
        elif choice == 2:
            print("List:  ", B)
            print("Result:", selection_sort(B))
        elif choice == 3:
            print("List:  ", C)
            print("Result:", insertion_sort(C))
        # elif choice == 4:
        #     print("List:  ", E)
        #     print("Result:", merge_sort(E))
        # elif choice == 5:
        #     print("List:  ", G)
        #     print("Result:", shell_sort(G))
        # elif choice == 6:
        #     print("List:  ", H)
        #     print("Result:", quick_sort(H))
        # elif choice == 7:
        #     print("List:  ", D)
        #     print("Result:", counting_sort(D))
        # elif choice == 8:
        #     print("List:  ", F)
        #     print("Result:", heap_sort(F))
        elif choice == 4:
            print("Bye!")
            break
        else:
            print("Enter correct value")
