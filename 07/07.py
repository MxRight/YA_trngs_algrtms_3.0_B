import datetime

def str_time(s:str):
    return datetime.datetime.strptime(s, '%H:%M:%S')

a, b, c = str_time(input()), str_time(input()), str_time(input())
delay = c - a
if delay.days==-1:
    delay+=datetime.timedelta(days=1)
half_delay = delay/2
sharp_time = b + half_delay
if half_delay.microseconds >= 500000:
    sharp_time+= datetime.timedelta(seconds=1)
    sharp_time = sharp_time.replace(microsecond=0)

print(sharp_time.time())
