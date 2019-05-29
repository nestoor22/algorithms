def counting_sort(A):

    B = [None] * len(A)
    C = [0] * (max(A)+1)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1

    C[0] -= 1

    for i in range(1, max(A)+1):

        C[i] = C[i] + C[i - 1
                        ]
    for j in range(len(A)):
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1

    return B


if __name__ == '__main__':
    print(counting_sort([9, 8, 7, 6, 5, 4, 3, 2, 1, 0, 1]))
