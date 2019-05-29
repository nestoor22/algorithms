import os
os.system("D:\\university\graplh4.png")
global dfs_num
def dfs(graph, start):
    dfs_num = {}
    num = 1
    stack, path = [start], []
    while stack:
        curr = stack.pop()
        if curr in path:
            continue
        path.append(curr)
        for neighbor in graph[curr]:
            stack.append(neighbor)
        dfs_num[curr] = num
        num += 1
    for k in dfs_num.keys():
        print(k,'->',dfs_num[k])
    return path

def bfs(graph, start):
    bfs_num = {}
    num = 1
    queue,path, = [start], []
    while queue:
        curr = queue.pop(0)
        if curr in path:
            continue
        path.append(curr)
        for neighbor in sorted(graph[curr]):
            queue.append(neighbor)
        bfs_num[curr] = num
        num +=1
    for k in bfs_num.keys():
        print(k,'->',bfs_num[k])
    return path

def dfs_recursive(graph, curr, path=None):
    path = [curr]
    for neighbor in graph[curr]:
        if neighbor not in path:
            path = dfs_recursive(graph, neighbor, path)
    for k in dfs_num.keys():
        print(k,'->',dfs_num[k])
    return path

def dfs_paths(graph, start, target):

    stack = [start]
    path = []
    while stack:
        curr = stack.pop()
        if curr in path:
            continue
        path.append(curr)
        for next in graph[curr]:
            if next == target:
                yield path + [next]
            else:
                stack.append(next)