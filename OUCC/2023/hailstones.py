#OUCC 2023 hailstones
#MPR-Nov 2023
#This scores 6 out of 6!  :)

#####################
# TASK              #

#Start with a number.

#If the number is even, divide the number by 2 to generate the next number.
#If the number is odd, multiply the number by 3 and add 1 to generate the next number.
#Repeat until the number is 1.
#For example: 5 → 16 → 8 → 4 → 2 → 1.

#It is believed that all hailstone sequences end with 1, no matter what the starting number is. 
#You are interested in the proportion of odd and even numbers in a hailstone sequence.

#Input format:
 #An integer.
#Output format:
 #Line 1: The number (integer) of even numbers in the sequence.
 #Line 2: The number (integer) of odd numbers in the sequence.

def Even(n):
  if(n%2==0):
    return True
  else:
    return False

num = int(input())

numList = []
numList.append(num)

while(num != 1):
  if(Even(num)):
    num = num//2
  else:
    num = num*3 + 1
  
  numList.append(num)
  
numEvens = 0
numOdds = 0
for someNum in numList:
  if(Even(someNum)):
    numEvens = numEvens + 1
  else:
    numOdds = numOdds + 1
print(numEvens)
print(numOdds)
    
