n, m = map(int, input().split())
lst = [[] for i in range(n + 1)]
flag = 'YES'

for i in range(m):
    a, b = map(int, input().split())
    if a != b:
        lst[a].append(b)
        lst[b].append(a)
    else:
        lst[a].append(b)


def dfs(graph, now, color):
    visited[now] = color
    for other in graph[now]:
        if other == color:
            return False
        if not visited[other]:
            dfs(graph, other, 3 - color)
    return True


visited = [0 for i in range(n + 1)]
for i in range(1, n + 1):
    if visited[i] == 0:
        dfs(lst, i, 1)

for i in range(1, n + 1):
    if lst[i]:
        for j in lst[i]:
            if visited[i] == visited[j]:
                flag = 'NO'
                break

print(flag)
