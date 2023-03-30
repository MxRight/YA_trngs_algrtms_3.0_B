from collections import deque
N, M, S, T, Q = list(map(int, input().split()))
blohi = [tuple(map(int, input().split())) for i in range(Q)]

def foo(N, M, S, T, goals):
    steps = [[-1 for _ in range(M + 1)] for _ in range(N + 1)]
    steps[S][T] = 0
    q = deque([(S, T)])
    head = 0
    moves = ((1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1))
    while head < len(q):
        x, y = q[head]
        lst = []
        for delta_x, delta_y in moves:
            new_x, new_y = x + delta_x, y + delta_y
            if (new_x > 0 and new_x <= N and new_y > 0 and new_y <= M and steps[new_x][new_y] == -1):
                lst.append((new_x, new_y))
                steps[new_x][new_y] = steps[x][y] + 1
        head += 1
        q.extend(lst)

    res = 0
    for x, y in goals:
        goal_steps = steps[x][y]
        if goal_steps == -1:
            return -1
        res += goal_steps
    return res

print(foo(N, M, S, T, blohi))
