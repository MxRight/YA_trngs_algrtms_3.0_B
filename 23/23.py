n = int(input())
dp = [0] * (n + 1)
prev = [0] * (n + 1)
dp[0] = 1

for i in range(2, n + 1):
    dp[i] = dp[i - 1]
    prev[i] = i - 1
    if i % 2 == 0 and dp[i // 2] < dp[i]:
        dp[i] = dp[i // 2]
        prev[i] = i//2
    if i % 3 == 0 and dp[i // 3] < dp[i]:
        dp[i] = dp[i // 3]
        prev[i] = i//3
    dp[i] += 1

print(dp[n])
res = [n]
x = n
dict_op = {'1':lambda x, y: y == x - 1,
           '2': lambda x, y: x%2 == 0 and y == x//2,
           '3': lambda x, y: x%3 == 0 and y == x//3
           }

while dp[x] != 0:
    n_x = prev[x]
    for k, v in dict_op.items():
        if v(x, n_x):
            if k == '3':
                n//=3
            elif k == '2':
                n//=2
            elif k == '1':
                n-=1
            res.append(n)
            break
    x = n_x
print(*res[::-1])
