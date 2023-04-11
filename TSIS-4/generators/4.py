a = int(input())
b = int(input())
def squrares(a,b):
    while a*a<b:
        yield a*a
        a+=1
for i in squrares(a,b):
    print(i)




"""for i in range (a,c):
    if a*a<c:
        print(a*a)
    a=a+1"""