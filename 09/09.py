n, m, k = map(int, input().split())
lst = [list(map(int, input().split())) for i in range(n)]
zapros = [tuple(map(int, input().split())) for i in range(k)]
res = 0

def prefix(lst: list):
    for i in range(len(lst)):
        last = 0
        for j in range(len(lst[i])):
            lst[i][j] += last
            last = lst[i][j]
    return lst

lst = prefix(lst)

def matrix_sum(tup):
    x1, y1, x2, y2 = tup
    res = 0
    for i in range(x1 - 1, x2):
        # print(lst[i][y2 - 1])
        if y1 - 2 >= 0:
            res += (lst[i][y2 - 1] - lst[i][y1 - 2])
        else:
            res+=lst[i][y2 - 1]
    return res


for i in range(k):
    print(matrix_sum(zapros[i]))
