# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 12:06:21 2017

@author: amylee00
"""
#this code will give you the lowest monthly credit card payment you should be making to pay off balance in a year

#change numbers here    
balance=4773 #initial balance at month 0
annualInterestRate= 0.2 #20%
numberOfMonths=12
fixedMonthlyPayment=10
monthlyInterestRate= annualInterestRate/12

#this is for convenience of the code
def_bal=balance 


while balance>0:

    balance=def_bal
    
    for i in range(1,numberOfMonths+1):
        
        balance=(balance-fixedMonthlyPayment)*(1+monthlyInterestRate)
        
    
    if balance>0:

        fixedMonthlyPayment +=10

    else:                
        print('Lowest Payment was: '+str(fixedMonthlyPayment))
        