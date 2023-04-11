farenheit = input()
def f_to_c(farenheit):
    celsius = (float(farenheit) - 32)*(5/9)
    return float(celsius)
print(f_to_c(farenheit))