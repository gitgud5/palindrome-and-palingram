#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Load file by using pre-made module named d_load.py
The function will return palingram words pair as a list which we will later print.

"""

from d_load import load


def palingrams(file):
    words = set(load(file))
    words_p = set()



    for word in words:
        r_word = word[::-1]
        length = len(word)
        if length>1:            
            for j in range(length):
                if word[j:] == r_word[:length-j] and r_word[length-j:] in words:
                    words_p.add((word, r_word[length-j:]))
                if word[:length-j] == r_word[j:] and r_word[:j] in words:
                    words_p.add((r_word[:j], word))
                    
                
    return words_p


a = sorted(palingrams("212.txt"))

for i, j in a:
    print(i,j)
