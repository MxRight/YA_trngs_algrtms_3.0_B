students = int(input())
k = int(input())
row, seat = int(input()), int(input())

def number_of_student(row, seat):
    return (row - 1) * 2 + seat

def num_to_seat(n):
    return n//2 + n%2, 2 if n%2==0 else 1

def two_vars(seat):
    res =  seat - k, seat + k
    fin = []
    for i in res:
        if students >= i > 0:
            fin.append(num_to_seat(i))
    if len(fin)==2:
        if abs(row - fin[0][0]) < abs(row - fin[1][0]):
            return fin[0]
        else:
            return fin[1]

    if len(fin) == 0:
        return (-1,)
    if len(fin) == 1:
        return fin[0]


print(*two_vars(number_of_student(row, seat)))
