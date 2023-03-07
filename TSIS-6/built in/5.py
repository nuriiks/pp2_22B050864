t=(False,True,False,)
def check(tuple):
    for i in tuple:
        if i == 0:
            return False
    return True
print(check(t))