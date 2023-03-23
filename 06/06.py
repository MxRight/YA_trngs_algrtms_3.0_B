m = int(input())
n = int(input())

size = 0
lst = []

for i in range(n):
    a, b = map(int, input().split())
    for n, j in enumerate(lst):
        if j!=0:
            c, d  = j
            if a<=d and c<=b:
                lst[n] = 0
                size-=1
    lst.append((a, b))
    size+=1

print(size)
