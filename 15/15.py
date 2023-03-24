n = int(input())
lst = list(map(int, input().split()))
stack = []

for i, v in enumerate(lst):
    while True:
        if stack != [] and stack[-1][1] > v:
            a, b = stack.pop()
            lst[a] = i
        else:
            break
    stack.append((i, v))

while stack!=[]:
    a, b = stack.pop()
    lst[a] = -1

print(*lst)
