text = input()
def function(text):
    text2 = text[::-1]
    if text==text2:
        return("palindrome")
    else:
        return("not palindrome")
print(function(text))
    