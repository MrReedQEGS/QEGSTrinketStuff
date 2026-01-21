import turtle

#Globals
topLeft = (-150,150)
KEY_LEN = 15
KEY_GAP = KEY_LEN/2

myKeyboard = [[0,["1","2","3","4","5","6","7","8","9","0","-","="]],
            [KEY_GAP,["Q","W","E","R","T","Y","U","I","O","P","{","}"]],
            [KEY_GAP*2,["A","S","D","F","G","H","J","K","L",";","'","#"]],
            [KEY_GAP,["\\","Z","X","C","V","B","N","M",",",".","/",]]]

#sub progs
def MyMove(someTurtle,xPos,yPos):
  someTurtle.penup()
  someTurtle.goto(xPos,yPos)
  someTurtle.pendown()

def MySquare(someTurtle,xPos,yPos,length):
  MyMove(someTurtle,xPos,yPos)
  
  for i in range(4):
    someTurtle.forward(length)
    someTurtle.left(90)

def MyKey(someTurtle,xPos,yPos,length,letterOrSymbol):
  LETTER_POS = length*0.27
  MySquare(someTurtle,xPos,yPos,length)
  
  #Now write the symbol in the middle of the key
  MyMove(someTurtle,xPos+LETTER_POS,yPos+LETTER_POS)
  someTurtle.write(letterOrSymbol,font=("Calibri", 8, "bold"))
  
#MAIN BODY
bob = turtle.Turtle()
bob.hideturtle()
bob.speed(0)

#Draw the outer rect
somePos = topLeft
MyMove(bob,somePos[0]-KEY_LEN,somePos[1]+KEY_LEN + KEY_GAP )
for i in range(2):
  bob.forward(300)
  bob.right(90)
  bob.forward(100)
  bob.right(90)

#Draw the keys
rowNum = 0

for row in myKeyboard:
  rowOffset = row[0]
  theKeys = row[1]
  somePos = (somePos[0] +rowOffset,somePos[1])
  rowNum = rowNum + 1
  
  #Draw the next row
  for i in range(len(theKeys)):
    MyKey(bob,somePos[0],somePos[1],KEY_LEN,theKeys[i])
    somePos = (somePos[0] + KEY_LEN +  KEY_GAP, somePos[1])

  somePos = (topLeft[0],somePos[1] - KEY_LEN - KEY_GAP)
