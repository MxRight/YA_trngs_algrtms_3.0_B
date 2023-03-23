max_symbol = 0
dict_s = dict()
not_allow = [' ', '\n']
with open('input.txt', encoding='utf-8') as f_in:
    for i in f_in.read():
        if i not in not_allow:
            if i not in dict_s:
                dict_s[i] = 0
            dict_s[i] += 1
            if dict_s[i] > max_symbol:
                max_symbol = dict_s[i]

res = sorted(dict_s)

for i in range(max_symbol, 0, -1):
    for j in res:
        if dict_s[j] >= i:
            print('#', end='')
        else:
            print(' ', end='')
    print()

print(''.join(res))
