"""
Load file
Then return the palindrome words as a list

"""

def load(file):
    with open(file) as f:
        a = f.read().strip().split('\n')
        pali = [i.lower() for i in a if i[:]==i[::-1] and len(i)>1]
        return pali



print(*load('2of12.txt'), sep='\n')
