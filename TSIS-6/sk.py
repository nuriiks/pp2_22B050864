import os
import re
def func(r):
    (x for x in r if x%2==1)
with open("data.txt","r") as file:
    data=file.read()
    rows=func(file)
    print(rows)
