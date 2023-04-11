n = int(input())
def f(n):
    value=0
    while value<n:
        if value%3==0 and value%4==0:
            yield value
        value += 1
for value in f(n):
    print(value)


"""for i in range(0,n):
    if i%3==0 and i%4==0:
        print(i)"""