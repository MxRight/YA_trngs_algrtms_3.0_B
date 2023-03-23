n = int(input())
letters = [0] * (n + 2)
for i in range(1, n + 1):
    letters[i] = int(input())
res = 0
for i in range(1, n+1):
    res+=min(letters[i], letters[i+1])

print(res)
