
def quicksort(A):
    if A == []:
        return []
    else:
        pivor = A[0]
        less = quicksort([x for x in A[1:] if x < pivor])
        greater = quicksort([x for x in A[1:] if x >= pivor])
        return less + [pivor] + greater


A = [45, 7845, 87, 56, 12, 11, 0, 148, 52, 35, 3]
print(quicksort(A))
