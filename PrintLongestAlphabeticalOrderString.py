# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 17:13:29 2017

@author: Amylee00
"""

s='abaaaaaab'
#  1234567890123456 just for reference only
counter=0
i=0
j=0
ans=[0]#storing counter in array
ans1=[]
ans2=[]

for i in range(len(s)):  
   if i<(len(s)-1):
         if ord(s[i])<= ord(s[i+1]):#using ascii numbers to compare order of alphabet
            counter +=1
#            print('counter:'+str(counter))
   
         else:
            counter +=1
#            print('else counter:'+str(counter))
            ans.append(counter)
   else:ans.append(len(s))       

for j in range(len(ans)):
    if j<(len(ans)-1):
        ans1.append(ans[j+1]-ans[j])
    
x=max(ans1)
y=ans1.index(x)
ans2.append(ans[y])
ans2.append(ans[y+1])
result=s[ans2[0]:ans2[1]]    
print('Longest substring in alphabetical order is: '+(result))