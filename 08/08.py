k = int(input())
min_x = 10e10
min_y = 10e10
max_x = max_y = 0
for i in range(k):
    x, y = map(int, input().split())
    min_x = min(min_x, x)
    max_x = max(max_x, x)
    min_y = min(min_y, y)
    max_y = max(max_y, y)

print(f'{min_x} {min_y} {max_x} {max_y}')
