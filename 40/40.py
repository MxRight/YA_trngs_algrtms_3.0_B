n = int(input())
m = int(input())

subway = {i: [] for i in range(1, n + 1)}

for line_num in range(m):
    line = list(map(int, input().split()))
    for i in line[1:]:
        subway[i].append(line_num)
a, b = list(map(int, input().split()))


def underground(m, subway_v, a, b):
    graph = [[] for _ in range(m)]
    for s, l in subway_v.items():
        if len(l) > 1:
            for i in l:
                graph[i].extend(l)
    b_l = subway_v[a]
    f_l = subway_v[b]
    if len(set(b_l).intersection(f_l)) > 0:
        return 0
    head = 0
    queue = b_l
    path = [-1 for _ in range(m)]
    for i in b_l:
        path[i] = 0
    while head < len(queue):
        other = graph[queue[head]]
        for cur in other:
            if path[cur] == -1:
                if cur in f_l:
                    return path[queue[head]] + 1
                path[cur] = path[queue[head]] + 1
                queue.append(cur)
        head += 1
    return -1


print(underground(m, subway, a, b))
