C = [2, 4, 14, 10, 8, 6, 18, 17, 11, 16]
H = [0, 5, 4, 7, 1, 22, 15, 12, 13, 6]

def extrack_min1(Q):
    minim = min(Q)
    index = Q.index(minim)
    return minim, index

def extrack_max(Q):
    for j in range(len(Q)):
        biggest = j
        for i in range(j+1, len(Q)):
            if Q[i] > Q[biggest]:
                biggest = i
        maxim = Q[biggest]
        index = Q.index(maxim)
        return maxim, index



def heap_sort_down(A):
    n = len(A)
    i = 0
    Q = A
    B = []
    while i < n :
        minim, index = extrack_max(Q)
        B.append(minim)
        del Q[index]
        i += 1
    return B

print(topologicalsort(A))
print(heap_sort_down(H))
