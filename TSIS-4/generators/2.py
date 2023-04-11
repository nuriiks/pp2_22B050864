n = int(input())
def f(n):
    value = 0
    while value<n:
        if value%2==0:
            yield value
        value += 1
for value in f(n):
    print(value,end= ',')




"""for i in range(0,n):
    if i%2==0:
        print(i, end = ', ')"""