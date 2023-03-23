stack = []
size = 0

while True:
    s = input()
    if s == 'exit':
        break
    if s[:2] == 'pu':
        n = int(s.split()[1])
        stack.append(n)
        size+=1
        print('ok')
    if s == 'size':
        print(size)
    if s == 'pop':
        if size>0:
            print(stack.pop())
            size-=1
        else:
            print('error')
    if s == 'clear':
        stack = []
        size = 0
        print('ok')
    if s == 'back':
        if size>0:
            print(stack[-1])
        else:
            print('error')

print('bye')
