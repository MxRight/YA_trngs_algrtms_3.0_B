n, m = map(int, input().split())
dp = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            dp[0][0] = dp[0][0]
        elif i == 0:
            dp[0][j] = dp[0][j - 1] + dp[0][j]
        elif j == 0:
            dp[i][0] = dp[i - 1][0] + dp[i][0]
        else:
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]

print(dp[-1][-1])
