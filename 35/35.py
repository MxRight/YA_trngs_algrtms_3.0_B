from sys import setrecursionlimit
setrecursionlimit(100000)
n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
visited = [0] * (n + 1)
path = []


def dfs(graph, colors, now, parent, ans):
    colors[now] = 1
    for i in range(n):
        if graph[now][i] == 1 and parent != i:
            if colors[i] == 0:
                is_cycled = dfs(graph, colors, i, now, ans)
                if is_cycled:
                    if now == ans[0]:
                        print("YES")
                        print(len(ans))
                        print(*[node + 1 for node in ans])
                        exit(0)
                    ans.append(now)
                    return True
            elif colors[i] == 1:
                ans.append(i)
                ans.append(now)
                return True
    colors[now] = 2
    return False


for i in range(n):
    if visited[i] == 0:
        dfs(graph, visited, i, -1, path)
print("NO")
