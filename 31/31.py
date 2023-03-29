n, m = map(int, input().split())
lst = [[] for i in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    if a!=b:
        lst[a].append(b)
        lst[b].append(a)
    else:
        lst[a].append(b)

def dfs(graph, visited, now):
    visited[now] = 1
    for other in graph[now]:
        if not visited[other]:
            dfs(graph, visited, other)

visited = [0 for i in range(n+1)]
dfs(lst, visited, 1)
s = sum(visited)
print(s)
for v, i in enumerate(visited):
    if i==1:
        print(v, end=' ')
