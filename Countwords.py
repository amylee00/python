# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:48:16 2017

@author: amylee00
"""
#count the word bob here, for example

s = "aosasoasoasbobobaoaosboboboooobob"

i=0
wordcounter=0

for i in range(len(s)):
    
    if s[i:i+3]=='bob':
        wordcounter +=1
    else:
        wordcounter +=0
        

print(wordcounter)

    