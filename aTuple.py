# -*- coding: utf-8 -*-
"""
Created on Fri Feb  3 20:03:18 2017

@author: amylee00
"""

def get_data(aTuple):
    nums=()
    words=()
    for t in aTuple:
        nums=nums+(t[0],) #nums is first element of the inner tuple
        if t[1] not in words: #if it's not already there in the tuple, add to the new word tuple
            words=words+(t[1],) #word is second element of the inner tuple
    min_nums=min(nums)
    max_nums=max(nums)
    unique_words=len(words) #this gives unique nunmber of words
    return (min_nums,max_nums,unique_words,words) 
    print(nums,words)

    
    
(small,large,numberofwords,words)=get_data(((1,'mine'),
                              (2,'yours'),
                              (3,'ours'),
                              (5,'mine')))    