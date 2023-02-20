n = int(input())
def f(n):
    value = 1
    while value*value <n:
        yield value*value
        value +=1
for value in f(n):
    print(value)