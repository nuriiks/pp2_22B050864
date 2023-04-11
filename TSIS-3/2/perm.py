from itertools import permutations
def permut(str2):
    return list(permutations(str2, len(str2)))

print(permut("abba"))