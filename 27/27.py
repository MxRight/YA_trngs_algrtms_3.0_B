n, m = map(int, input().split())
dp = [list(map(int, input().split())) for i in range(n)]
prev = [[0] * m for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = dp[0][0]
            prev[0][0] = -1
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + dp[0][j]
            prev[0][j] = 0
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + dp[i][0]
            prev[i][0] = 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]
            if dp[i - 1][j] >= dp[i][j - 1]:
                prev[i][j] = 1
            else:
                prev[i][j] = 0

print(dp[-1][-1])
i, j = n - 1, m - 1
res_var = []
while i > 0 or j > 0:
    if prev[i][j] == 1:
        i -= 1
        res_var.append('D')
    else:
        j -= 1
        res_var.append('R')

for i in range(len(res_var) - 1, -1, -1):
    print(res_var[i], end=' ')
