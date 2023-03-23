n = int(input())
stickers = sorted(set(map(int, input().split())))
k = int(input())
k_stickers = list(map(int, input().split()))

def bin_finder(lst, i):
    l = 0
    r = len(lst) - 1
    while l < r:
        m = (l + r) // 2
        if lst[m] >= i:
            r = m
        else:
            l = m + 1
    return r


for i in k_stickers:
    if i <= stickers[0]:
        print(0)
    elif i > stickers[-1]:
        print(len(stickers))
    else:
        print(bin_finder(stickers, i))
