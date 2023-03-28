n = int(input())
if n == 0:
    print(0)
    print(0, 0)
else:
    days_cost = [int(input()) for i in range(n) if n > 0]

    dp = [[0 for _ in range(n)] for _ in range(n + 1)]
    for i in range(1, n):
        dp[0][i] = 32000



    for i in range(1, n + 1):
        for j in range(n):

            if days_cost[i - 1] <= 100:
                if 0 <= j + 1 <= n - 1:
                    dp[i][j] = min(dp[i - 1][j] + days_cost[i - 1], dp[i - 1][j + 1])
                else:
                    dp[i][j] = dp[i - 1][j] + days_cost[i - 1]
            elif days_cost[i - 1] > 100:
                if 0 <= j + 1 <= n - 1:
                    dp[i][j] = min(dp[i - 1][j - 1] + days_cost[i - 1], dp[i - 1][j + 1])
                else:
                    dp[i][j] = dp[i - 1][j - 1] + days_cost[i - 1]


    res = min(dp[n])
    print(res)
    k1 = dp[n].index(res)
    for i in range(k1, n):
        if dp[n][k1] == dp[n][i]:
            k1 = i
    k2 = 0
    path = []

    indx = k1

    if n>1:
        while n!=1:
            if dp[n][indx] - dp[n-1][indx] == days_cost[n-1]:
                    indx = indx
            elif dp[n][indx] - dp[n-1][indx - 1] == days_cost[n-1]:
                    indx = indx - 1
            elif dp[n][indx] == dp[n-1][indx + 1]:
                path.append(n)
                indx = indx + 1
                k2+=1


            n-=1
    else:
        if days_cost[0]>100:
            k1 = 1


    print(k1, k2)
    for i in sorted(path):
        print(i)

