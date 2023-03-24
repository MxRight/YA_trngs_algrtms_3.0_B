first = list(map(int, input().split()))
second = list(map(int, input().split()))
head_f = 0
head_s = 0
size_f = 5
size_s = 5
number = 0

while True:
    if number>10e6:
        print('botva')
        break
    if size_f == 0:
        print(f'second {number}')
        break
    if size_s == 0:
        print(f'first {number}')
        break

    if (first[head_f]==0 and second[head_s]==9) or (first[head_f] > second[head_s] and (first[head_f]!=9 or second[head_s]!=0)):
        first.append(first[head_f])
        first.append(second[head_s])
        head_s+=1
        head_f+=1
        size_f+=1
        size_s-=1

    elif (first[head_f]==9 and second[head_s]==0) or (second[head_s] > first[head_f] and (first[head_f]!=0 or second[head_s]!=9)):
        second.append(first[head_f])
        second.append(second[head_s])
        head_s+=1
        head_f+=1
        size_s+=1
        size_f-=1
    number+=1
