# -*- coding: utf-8 -*-
"""
Created on Fri Jan 20 19:48:16 2017

@author: chikam88
"""

s = 'abc' #string

vowel='a','e','i','o','u' #list of vowels

counter = 0 #initiate counter
vowcount = 0 #initiate counter

for counter in range(len(s)):

    if str(s[counter]) in str(vowel):
        vowcount += 1
    else:
        vowcount += 0

print('number of vowels: '+ str(vowcount))
        
