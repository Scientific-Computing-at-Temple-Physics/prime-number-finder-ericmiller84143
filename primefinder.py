#Eric Miller
#1-26-2018
#This code prints all prime numbers between (and including) the numbers entered initially.

import math as ma

#Ask for lower (x1) and upper (x2) limits; print these to screen
x1 =  input('smallest number to check: ')
print "Lower Limit:", x1

x2 = input('largest number to check: ')
print "Upper Limit:", x2 

print "Primes from", x1, "to", x2, "are:"

for i in range(x1, x2 + 1):  #range over x1, (x1) + 1, (x1) +2, ... , x2
    if i == 1:              #the number 1 is not prime
        continue            #if a 1 comes up, skip this iteration and move on
    for j in range(2, int(ma.sqrt(i))+1)  #check if integers 2 < j < i-1 are factors of i
        if i%j==0:                        #if none in that range, there can't be any greater
            break           #break loop if a divisor is found
    else:                   #if i has no divisors, it is prime so print it to the screen
        print i
