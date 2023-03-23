input_str = input()
dict_str = dict()
l = len(input_str)

for i in range(l):
    if input_str[i] not in dict_str:
        dict_str[input_str[i]] = 0
    dict_str[input_str[i]] += (l - i) * (i + 1)

for i in sorted(dict_str.keys()):
    print(f'{i}: {dict_str[i]}')
