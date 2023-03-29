import sys
sys.setrecursionlimit(200000)

n, m = map(int, input().split())
lst = [[] for i in range(n + 1)]
flag = False

for i in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)

visited = [0 for i in range(n + 1)]
path = []

def dfs(graph, now):
    global flag
    visited[now] = 1
    for other in graph[now]:
        if visited[other] == 1:
            flag = True
            path.append(now)
        if not visited[other]:
            dfs(graph, other)
    visited[now] = 2
    path.append(now)
    return True

for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(lst, i)


if flag:
    print(-1)
else:
    for i in range(n - 1, -1, -1):
        print(path[i], end=' ')
