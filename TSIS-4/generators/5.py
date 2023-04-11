n = int(input())
def f(n):
    while n>0:
        yield n
        n-=1
for val in f(n):
    print(val)


"""for i in range(0,n):
    my_list.append(i)
print(my_list[::-1])"""