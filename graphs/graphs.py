from labs import *

if __name__ == "__main__":

    graph1 = {
        'A': {'B','C'},
        'B': {'A','E','M'},
        'C': {'A','D','F'},
        'D': {'C'},
        'E': {'B','G'},
        'F': {'C','H','M'},
        'G': {'E','K','M'},
        'H': {'F','M'},
        'K': {'G'},
        'M': {'B','F','G','H'}
    }
    print("Введіть 'd',щоб виконати обхід в глибину, 'r',щоб виконати рекурсивний обхід в глибину\n"
        "'b',щоб виконати обхід в ширину, 's', щоб знайти шлях до вершини,'e',щоб вийти: ")
    while True:
        i = input()
        if i == 'd':
            s = input("Вкажіть початкову вершину: ")
            print(dfs(graph1,s))
        elif i == 'r':
            s = input("Вкажіть початкову вершину: ")
            print(dfs(graph1, s))
        elif i == 'b':
            s = input("Вкажіть початкову вершину: ")
            print(bfs(graph1, s))
        elif i == 's':
            s = input("Вкажіть початкову вершину: ")
            t = input("Вкажіть кінцеву вершину: ")
            print(list(dfs_paths(graph1,s,t)))
        else:
            print("BYE!")
            break