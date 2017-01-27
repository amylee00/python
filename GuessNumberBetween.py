# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 13:39:58 2017

@author: Administrator
"""

x=100
low=0
high=x
numGuesses=0
guess=int((high+low)/2)
counter=0

print('Please think of a number between '+str(low)+' and '+str(high)+'!')
print('Is your number'+str(guess)+'?')
res=input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correct.:')

while counter < x:    
    
    if res=='h':
            numGuesses +=1
            high=guess
            guess=int((guess+low)/2)    
            print('Is your secret number'+str(guess)+'?')
            res=input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate the answer is correct.:')
            counter +=1
            
    elif res=='l':
            numGuesses +=1
            low=guess
            guess=int((high+low)/2)
            print('Is your secret number'+str(guess)+'?')
            res=input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate the answer is correct.:')       
            counter +=1
    
    elif res=='c':
        
            print('Game over. Your secret number was: '+str(guess))
            break
         
    else:
            print('Sorry, I did not understand your input')
#            print('Please think of a number between '+str(low)+' and '+str(high)+'!')
            print('Is your secret number'+str(guess)+'?')
            res=input('Enter \'h\' to indicate the guess is too high. Enter \'l\' to indicate the guess is too low. Enter \'c\' to indicate I guessed correct.:')
            counter +=0