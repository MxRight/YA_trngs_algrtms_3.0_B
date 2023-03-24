head = 0
qu = []
size = 0
while True:
    s = input()
    if s == 'exit':
        print('bye')
        break
    if s[:2] == 'pu':
        qu.append(int(s.split()[-1]))
        size+=1
        print('ok')
    if s == 'pop':
        if size>0:
            print(qu[head])
            head+=1
            size-=1

        else:
            print('error')
    if s == 'size':
        print(size)

    if s == 'clear':
        qu = []
        size = 0
        head = 0
        print('ok')
    if s == 'front':
        if size>0:
            print(qu[head])
        else:
            print('error')
