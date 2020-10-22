#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Load file by using pre-made module named d_load.py
The function will return palingram words pair as a list which we will later print.

"""

from d_load import load


def palingrams(file):
    words = load(file)
    words_p = []



    for word in words:
        r_word = word[::-1]
        length = len(word)
        if length>1:            
            for j in range(length):
                if word[j:] == r_word[:length-j] and r_word[length-j:] in words:
                    words_p.append((word, r_word[length-j:]))
                    
                
    return words_p


a = sorted(palingrams("212.txt"))

for i, j in a:
    print(i,j)
