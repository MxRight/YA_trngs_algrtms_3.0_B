n = int(input())
n_lst = list(map(int, input().split()))
m = int(input())
m_lst = list(map(int, input().split()))
dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if n_lst[i - 1] == m_lst[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])



res = []
i = n
j = m
while i > 0 and j > 0:
    if n_lst[i - 1] == m_lst[j - 1]:
        res.append(n_lst[i - 1])
        i -= 1
        j -= 1
    elif dp[i - 1][j] == dp[i][j]:
        i -= 1
    else:
        j -= 1

print(*res[::-1])
