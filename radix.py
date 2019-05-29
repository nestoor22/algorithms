def counting_sort(A, digit, radix):

    B = [0]*len(A)
    C = [0]*int(radix)
    for i in range(0, len(A)):
        C[(A[i]//radix**digit) % radix] = C[(A[i]//radix**digit) % radix] + 1

    for j in range(1,radix):
        C[j] = C[j] + C[j-1]
    for m in range(len(A)-1, -1, -1):
        C[(A[m]//radix**digit)%radix] = C[(A[m]//radix**digit)%radix] -1
        B[C[(A[m]//radix**digit)%radix]] = A[m]
    return B


def radix_sort(A, radix):
    for i in range(3):
        return counting_sort(A, i, radix)


A = [12, 656, 666, 123, 122, 874, 574]
print(radix_sort(A, 10))

