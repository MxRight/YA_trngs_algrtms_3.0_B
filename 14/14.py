n = int(input())
s = list(map(int, input().split()))
train = []
l = len(s)
for i in range(l):
    train.append(s.pop())
nummer = 1
stack1, stack2 = [], []
size = 0
stack_1_last = 0

while True:
    if len(train) > 0 and stack_1_last != nummer:
        stack_1_last = train.pop()
        stack1.append(stack_1_last)
        size+=1
    if size > 0 and stack_1_last == nummer:
        stack2.append(stack1.pop())
        nummer += 1
        size -= 1
        if size > 0:
            stack_1_last = stack1[-1]
    if len(stack1) == len(train) == 0:
        print('YES')
        break
    if len(train) == 0 and stack2[-1]+1!=stack1[-1]:
        print('NO')
        break
