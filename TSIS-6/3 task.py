import re
text = input()
x = re.sub("[0-9]{3}","*",text)
print(x)




#ex2
def func():
    i=1
    if i%2==0:
        yield  i*i
    i +=1

#ex3
#nope

