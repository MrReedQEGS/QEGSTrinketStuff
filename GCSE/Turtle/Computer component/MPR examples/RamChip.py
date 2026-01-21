import turtle

#SUB PROGRAMS
def DrawRectangle(theTurtle,somePosition,length,width,colour = "none"):
  
  MoveWithoutDrawing(bob,somePosition)
  
  if(colour != "none"):
    theTurtle.fillcolor(colour)
    theTurtle.begin_fill()

  for i in range(2):
    theTurtle.forward(length)
    theTurtle.left(90)
    theTurtle.forward(width)
    theTurtle.left(90)

  if(colour != "none"):
    theTurtle.end_fill()

def DrawRamChip(theTurtle,somePosition,length,width,colour = "none"):
  DrawRectangle(theTurtle,somePosition,length,width,colour)
  #Now draw the white wires on the left of the chip
  MoveWithoutDrawing(bob,somePosition)
  theTurtle.setheading(180)
  theTurtle.color("white")
  newPos = somePosition
  for i in range(16):
    theTurtle.backward(3)
    theTurtle.forward(6)
    newPos = (newPos[0],newPos[1] + width/15)
    MoveWithoutDrawing(bob,newPos)
  
  
  #Now draw the white wires on the right of the chip
  newPos = (somePosition[0]+ length,somePosition[1])
  MoveWithoutDrawing(bob,newPos)
  theTurtle.setheading(0)
  theTurtle.color("white")
  
  for i in range(16):
    theTurtle.backward(3)
    theTurtle.forward(6)
    newPos = (newPos[0],newPos[1] + width/15)
    MoveWithoutDrawing(bob,newPos)
  
  #reset everything so next chip is in the correct place.
  MoveWithoutDrawing(bob,somePosition)
  theTurtle.setheading(0)
  theTurtle.color(colour)

def MoveWithoutDrawing(theTurtle,somePos):
  theTurtle.penup()
  theTurtle.setpos(somePos[0],somePos[1])
  theTurtle.pendown()
 
 
#MAIN BODY
instantDrawing = True
    
bob = turtle.Turtle()
bob.speed(0)
#screen = turtle.Screen()
#screen.setup(800,600)

if(instantDrawing):
  bob.tracer(0,0)
  
#draw outer shape
DrawRectangle(bob,(-100,0),220,70,"green")

#draw some chips
chipWidth = 14
chipHeight = 50
numOfChips = 8
chipColour = "black"

for i in range(numOfChips):
  pos = (-80+(i*(chipWidth+10)),15)
  DrawRamChip(bob,pos,chipWidth,chipHeight,chipColour)
  
  if(instantDrawing):
    bob.update()

#copper connectors drawn in 3 groups across the bottom of the chip
numOfConnectorsSection1 = 8
numOfConnectorsSection2 = 11
numOfConnectorsSection3 = 15
connectorWidth = 5
connectorHeight = 8
connectorColour = "yellow"

for i in range(numOfConnectorsSection1):
  DrawRectangle(bob,(-90+(i*(connectorWidth)),0),connectorWidth,connectorHeight,connectorColour)
  
  if(instantDrawing):
    bob.update()

for i in range(numOfConnectorsSection2):
  DrawRectangle(bob,(-40+(i*(connectorWidth)),0),connectorWidth,connectorHeight,connectorColour)
  
  if(instantDrawing):
    bob.update()
 
for i in range(numOfConnectorsSection3):
  DrawRectangle(bob,(30+(i*(connectorWidth)),0),connectorWidth,connectorHeight,connectorColour)
  
  if(instantDrawing):
    bob.update()
  
#Add some labelling
MoveWithoutDrawing(bob,(0,-35))
bob.fillcolor("black")
bob.write("copper connectors")
MoveWithoutDrawing(bob,(15,-25))
bob.setheading(110)
bob.forward(30)

fred = turtle.Turtle()
MoveWithoutDrawing(fred,(-120,100))
fred.fillcolor("black")
fred.write("Random access memory (RAM)",font=("Arial", 14, "normal"))
fred.hideturtle()

harry = turtle.Turtle()
MoveWithoutDrawing(harry,(130,50))
harry.write("memory chip")
MoveWithoutDrawing(harry,(130,50))
harry.fillcolor("black")
harry.setheading(185)
harry.forward(30)

if(instantDrawing):
  bob.update()




  
