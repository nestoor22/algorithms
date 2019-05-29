def search_min(tr, vizited):#1 место для оптимизации
    min=max(tr)
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem>0 and elem<min and index not in vizited:
                min=elem#веса путей
                index2=index# индекс города
    return [min, index2]

def prim(matr):
    toVisit=[i for i in range(1,len(matr))]# города кроме начального(0)
    vizited=[0]
    result=[0]# начнем с минска
    for index in toVisit:
        weight, ind=search_min(matr, vizited)
        result.append(weight)#в результат будут заноситься веса
        vizited.append(ind)# содержит карту пути
    return result