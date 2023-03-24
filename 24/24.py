n = int(input())
lst = [[0] * 3 for i in range(n + 3)]
dp = [0] * (n + 3)
for i in range(3):
    lst[i][0] = lst[i][1] = lst[i][2] = 3601


for i in range(3, n + 3):
    a, b, c = map(int, input().split())
    lst[i][0] = a
    lst[i][1] = b
    lst[i][2] = c
    dp[i] = min(dp[i-1] + a, dp[i - 2] + lst[i-1][1], dp[i - 3] + lst[i-2][2])

print(dp[-1])
