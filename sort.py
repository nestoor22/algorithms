def partitation(A, p, r):
    i = p - 1
    piv = A[r]
    for j in range(p,r):
        if A[j] <= piv:
            i = i+1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1


def quickSort(A, p, r):
    if p < r:
        q = partitation(A, p, r)
        quickSort(A, p, q-1)
        quickSort(A, q+1, r)
    return A

if __name__ == '__main__':
    A = [5, 4, 3, 1, 2, 8, 9, 6, 0, 7]
    n = len(A)
    print('List:', A)
    print('Result:', quickSort(A, 0, n-1))