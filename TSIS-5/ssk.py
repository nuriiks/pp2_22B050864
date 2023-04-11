import os, re
text = input()
if not os.path.exists("c:\\Users\\nuriks\\Documents\\GitHub\\pp2_22B050864\\lox.txt"):
    open("dias.txt","x")
with open("dias.txt","w") as l:
    l.writelines(text)
with open("dias.txt","r") as gay:   
    data=gay.read()         
    if re.findall("pidor",data):
        print("Yes")
    else:
        print("No")