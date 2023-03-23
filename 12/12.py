def check(str):
    stack = []
    left = ['(', '[', '{']
    right = [')', ']', '}']
    no = 'no'
    for char in str:
        if char not in left + right:
            continue
        if char in left:
            stack.append(char)
        else:
            if not stack:
                return no
            top = stack.pop()
            var_left = left.index(top)
            if char != right[var_left]:
                return no
    if not stack:
        return 'yes'
    else:
        return 'no'


print(check(input()))
