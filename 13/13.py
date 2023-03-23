from operator import mul, add, sub
s = input().split()
l = len(s)
abc = [s.pop() for i in range(len(s))]
stack = []
res = 0
def calc(znak, a, b):
    znak_dict = {'+': add(a, b), '-':sub(a, b), '*':mul(a, b)}
    return znak_dict[znak]

for i in range(l):
    symb = abc.pop()
    if symb in ['+', '-', '*']:

        b, a = stack.pop(), stack.pop()
        stack.append(calc(symb, a, b))
    else:
        stack.append(int(symb))

print(*stack)
