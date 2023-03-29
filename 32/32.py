from threading import stack_size
import sys
sys.setrecursionlimit(200000)
# mb = 1024 * 1024
# stack_size(255 * mb)

with open('input.txt', 'r', encoding='utf-8') as f_in:
    n, m = map(int, f_in.readline().split())
    lst = [[] for i in range(n + 1)]
    set_vertex = set()

    for i in range(m):
        a, b = map(int, f_in.readline().split())
        if a != b:
            lst[a].append(b)
            lst[b].append(a)
        else:
            lst[a].append(b)
        set_vertex.add(a)
        set_vertex.add(b)


def dfs(graph, start, k):
    stack = [start]
    temp = set()
    while stack:

        vertex = stack.pop()
        temp.add(vertex)
        if visited[vertex] == 0:
            visited[vertex] = k
            stack.extend(graph[vertex])
    return sorted(temp)



visited = [0 for i in range(n + 1)]
k = 0

k_count = 0
k_sum = 0
fin = []
for i in range(1, n + 1):
    if i in set_vertex and visited[i] == 0:
        k += 1
        res = dfs(lst, i, k)
        l_res = len(res)
        k_count += 1
        k_sum += l_res
        fin.append((l_res, res))
    if i not in set_vertex:
        fin.append((1, [i]))

print(n - k_sum + k_count)
for a, b in fin:
    print(a)
    print(*b)
