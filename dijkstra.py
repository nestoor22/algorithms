G = [[0, 6, 4, 0, 0],
     [0, 0, 2, 3, 0],
     [0, 1, 0, 9, 3],
     [0, 0, 0, 0, 4],
     [7, 0, 0, 5, 0]]


def search(G,ind):
    shortest2 = []
    index2 = []
    for j in range(len(G[ind])):
        if G[ind][j] != 0:
            minim = G[ind][j]
            shortest2.append(minim)
            index2.append(G[ind].index(minim))
    return shortest2, index2



def dijkstra(G, s):
    shortest = [0] * len(G)
    pred =[s]
    for ind in pred:
        minim, index = search(G,ind)
        for i in minim:
            for j in index:
                if j not in pred:
                    if shortest[ind] > i:
                        shortest[ind] = i
                        pred[ind] = j
    return shortest, pred


print(dijkstra(G,0))




