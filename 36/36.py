from collections import deque

n = int(input())
graph = [list(map(int, input().split())) for i in range(n)]
start, finish = map(int, input().split())

visited = [-1] * (n + 1)

def bfs(v=start):
    deq = deque([v])
    visited[v] = 0
    while deq:
        cur = deq.popleft()
        for i, v in enumerate(graph[cur - 1]):
            if v == 1 and visited[i + 1] == -1:
                visited[i + 1] = visited[cur] + 1
                deq.append(i + 1)

bfs()
print(visited[finish])
