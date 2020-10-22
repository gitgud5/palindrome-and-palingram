"""
Load file by using pre-made module
The function will return palindrome words as a list

"""
from d_load import load

def palindromes(file):
    l = load(file)
    a = []
##    For loop appends palindromes to list 
    for i in l:
        if i==i[::-1] and len(i)>1:
            a.append(i.capitalize())
    return a


a = palindromes("2of12.txt")

print(*a, sep="  ")
