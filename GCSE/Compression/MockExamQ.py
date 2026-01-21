#Mr Reed - 19/6/25
#RLE a given input string - Mock exam edition

#theString = input("String to compress: ")
#theString = input("String to compress: "
#theString = Input("String to compress: ")
#theString = input("")


#answerString = ""
#answerString = []
#answerString = 0
#answerString = False

#Grab the first letter in the string
#previousLetter = theString[0]
#previousLetter = theString[first]
#previousLetter = theString[1]
#previousLetter = theString.0

#Now process through the whole string looking for "runs" of the same letter
pos = 1
count = 1

#while(pos < len(theString)):
#while(pos < len(theString)):
#while(pos < len(theString)):
#while(pos < len(theString)):
  
  #Grab the next letter
  nextLetter = theString[pos]
  
  #Is it the same letter?
  if(nextLetter == previousLetter):
    count = count + 1
  else:
    answerString = answerString + str(count)+ previousLetter
    count = 1
    
  #Move on to the next letter.  
  pos = pos + 1  
  previousLetter=nextLetter
  
#Tag the last bit on
answerString = answerString + str(count) + previousLetter
print(answerString)
