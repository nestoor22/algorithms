def search_min(tr, vizited):#1 ����� ��� �����������
    min=max(tr)
    for ind in vizited:
        for index, elem in enumerate(tr[ind]):
            if elem>0 and elem<min and index not in vizited:
                min=elem#���� �����
                index2=index# ������ ������
    return [min, index2]

def prim(matr):
    toVisit=[i for i in range(1,len(matr))]# ������ ����� ����������(0)
    vizited=[0]
    result=[0]# ������ � ������
    for index in toVisit:
        weight, ind=search_min(matr, vizited)
        result.append(weight)#� ��������� ����� ���������� ����
        vizited.append(ind)# �������� ����� ����
    return result