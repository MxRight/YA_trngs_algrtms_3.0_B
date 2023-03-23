with open('input.txt', 'r') as f_in:
    k = int(f_in.readline())
    s = f_in.readline().strip()

# k = int(input())
# s = input()

def foo(s: str, symb: str, k: int):
    l = -1
    r = -1
    max_res = 0
    while True:
        if k >= 0 and r<= len(s) - 2:
            r += 1
            if s[r] != symb:
                k -= 1
        else:
            l += 1
            if s[l] != symb:
                k += 1
            if k>0:
                max_res = max(max_res, r - l + k)
            else:
                max_res = max(max_res, r - l)
            if r == len(s) - 1:
                # print(k, max_res)
                return max_res


res = 0
for i in set(s):
    res = max(res, foo(s, i, k))

print(res)
