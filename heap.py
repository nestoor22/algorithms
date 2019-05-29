
def parent(i):
    return i//2


def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2


def MaxHeapify(A,n, i):
    largest = i
    l = left(i)
    r = right(i)
    if l < n and A[i] < A[l]:
        largest = l
    if r < n and A[largest] < A[r]:
        largest = r
    if largest != i:
        A[i], A[largest] = A[largest], A[i]
        MaxHeapify(A, n, largest)


def buildMaxHeap(A):
    n = len(A)
    for i in range(n//2, -1, -1):
        MaxHeapify(A, n, i)


def heapSort(A):
    n = len(A)

    for i in range(n-1, -1, -1):
        A[i], A[0] = A[0], A[i]
        MaxHeapify(A, i, 0)


def HeapMaximum(A):
    return A[0]


def HeapExtractMax(A):
    if len(A) < 1:
        return "Черга порожня"
    max = A[0]
    A[0], A[len(A)-1] = A[len(A)-1], A[0]
    A.remove(max)
    MaxHeapify(A, len(A), 0)


def HeapIncreaseKey(A, i, key):
    if key < A[i]:
        return "Новий ключ менше поточного"
    A[i] = key
    while i > 0 and A[parent(i)] < A[i]:
        A[i], A[parent(i)] = A[parent(i)], A[i]
        i = parent(i)


def MaxHeapInsert(A, key):
    A.append(float('-inf'))
    n = len(A)-1
    HeapIncreaseKey(A, n, key)


if __name__ == '__main__':

    A = [87, 56, 32, 451, 45, 75, 421]
    buildMaxHeap(A)
    print("Heap:", A)
    MaxHeapInsert(A, 123)
    print("Heap insert 123:", A)





