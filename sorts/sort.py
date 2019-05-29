def insertion_sort(A):
    for i in range(1, len(A)):
        while (i > 0) and (A[i] < A[i-1]):
             A[i], A[i-1] = A[i-1], A[i]
             i -= 1
    return A


def selection_sort(A):
    n = len(A)
    for i in range(n):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
    return A


def bubble_sort(A):
    n = len(A)
    m = 0
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if A[j] >= A[j+1]:
                m += 1
                A[j], A[j+1] = A[j+1], A[j]
                swapped = True
        if not swapped:
            return A
    return A


# def counting_sort(A):
#     m = max(A) + 1
#     count = [0] * m
#     for j in A:
#         count[j] += 1
#     i = 0
#     for a in range(m):
#         for c in range(count[a]):
#             A[i] = a
#             i += 1
#     return A
#
#
# def shell_sort(A):
#
#     sublist_count = len(A) // 2
#     while sublist_count > 0:
#
#         for start_position in range(sublist_count):
#             gap_insertion_sort(A, start_position, sublist_count)
#         sublist_count //= 2
#     return A
#
#
# def gap_insertion_sort(A, start, gap):
#     for i in range(start+gap, len(A), gap):
#         current_value = A[i]
#         position = i
#         while position >= gap and A[position-gap] > current_value:
#             A[position] = A[position-gap]
#             position = position-gap
#
#         A[position] = current_value
#
#
# def quick_sort(A):
#     if A == []:
#         return []
#     else:
#         average = A[0]
#         less = quick_sort([x for x in A[1:] if x < average])
#         greater = quick_sort([x for x in A[1:] if x >= average])
#         return less + [average] + greater
#
#
def merge_sort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left_half = A[:mid]
        right_half = A[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i, j, k = 0, 0, 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                A[k] = left_half[i]
                i += 1
            else:
                A[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            A[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            A[k] = right_half[j]
            j += 1
            k += 1
    return A

#
# def heapify(A, n, i):
#     largest = i
#     l = 2*i + 1
#     r = 2*i + 2
#     if l < n and A[largest] < A[l]:
#         largest = l
#     if r < n and A[largest] < A[r]:
#         largest = r
#     if largest != i:
#         A[i], A[largest] = A[largest], A[i]
#         heapify(A, n, largest)
#
#
# def heap_sort(A):
#     n = len(A)
#     for i in range(n, -1, -1):
#         heapify(A, n, i)
#     for i in range(n-1, 0, -1):
#         A[i], A[0] = A[0], A[i]
#         heapify(A, i, 0)
#     return A