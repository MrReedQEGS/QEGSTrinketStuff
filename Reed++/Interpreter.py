#Reed ++ v0.2
#This is the interpreter for the new language Reed ++
#Now with even more stupid syntax ♣ ∞  ...enjoy

#a dictionary used to store any variables that are needed
#only ints and strings work at the moment
someFile = "new.red"
myVars = {}

def Interpret(someLine):
  if(someLine == ""):
    return
  
  command =someLine[0]
  rest = someLine[1:]
  
  if(command == "♣"):
    #it is a comment
    return
  elif(command == "<"):
    #its an input statement with a type, variable name and prompt
    bits = rest.split("#")
    varType = bits[0]
    varName = bits[1]
    prompt = bits[2]
    
    ans = input(prompt)
    if(varType == "I"):
      myVars[varName] = int(ans)
    elif(varType == "S"):
      myVars[varName] = ans
    
  elif(command == "#"):
    #its a variable declaration int and string work so far
    bits=rest.split("#")
    varName = bits[1]
    varType = bits[0]
    varValue = bits[2]
    if(varType == "I"):
      myVars[varName] = int(varValue)
    elif(varType == "S"):
      myVars[varName] = varValue
  
  elif(command == "►" or command == "→"):
    #It is a print command...take care it may need
    #a new line too!
    if(rest[0]=="*"):
      #print contents of variable!!!
      rest=rest[1:]
      print(str(myVars[rest]),end="")
    else:
      #it is not a variable, so just print it.
      print(rest,end = "")

    #If it is a new line print then start a new line!      
    if(command == "►"):
      print("")
      
  elif(command == "∞"):
    #its a for loop!
    loopnums = rest.split(",")
    start = loopnums[0]
    end = loopnums[1]
    if(start.isdigit() == False):
      #its an int variable stored in the dict
      start = myVars[start]
      
    if(end.isdigit() == False):
      #its an int variable stored in the dict
      end = myVars[end]
  
    #the loop commands are between sq brackets
    loopcomms = loopnums[2]
    loopcomms = loopcomms[1:]
    loopcomms = loopcomms[:len(loopcomms)-1]
    commList = loopcomms.split("!")
    for i in range(start,end+1):
      for comm in commList:
        Interpret(comm)
    
f=open(someFile,"r")
code = f.readlines()
for line in code:
  Interpret(line.rstrip("\n"))

if(myVars["debug"] == "ON"): 
  print("********")
  print("* VARS *")
  print("********")
  print(myVars)
