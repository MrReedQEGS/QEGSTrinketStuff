#Mr Reed 26/2/24
# aaaaaabbaaabbbbbbbbbbbxxxxxx
# is  a6b2a3b11x6

#Split the compressed string into pairs of letters and numbers.  
#The number part can be multi digit..be careful to take account of this.  It could be a10 with 2 digit num!!
#Assume the letter part is at most one char long.

theString = "a10b2a3b11x6a1c4v2"
pos = 0

lenOfString = len(theString)

print("RLE Compressed string:")
print(theString)
print()

print("Decompressed string:")

#Loop through the whole string looking for pairs of letters and numbers
while(pos < lenOfString):
  #Get the current letter
  currentLetter = theString[pos]
  pos = pos + 1
  numberString = ""
  #Now find the number that goes with it.
  for i in range(pos,lenOfString):
    nextThing = theString[i]
    if(nextThing.isdigit() == False):
      #We have found the end of the digits that go with this letter
      break
    else:
      numberString = numberString + nextThing
      pos = pos + 1
      
  #now print out the current letter the right number of times...on the same line    
  number = int(numberString)
  for j in range(number):
    print(currentLetter,end="")
