n = int(input())
lst = sorted(map(int, input().split()))

dp = [[0, 0] for _ in range(n)]
dp[1][0] = lst[1] - lst[0]
dp[1][1] = lst[1] - lst[0]

for i in range(2, n):
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][1]) + (lst[i] - lst[i - 1])
    dp[i][0] = dp[i - 1][1]

print(dp[n-1][1])
