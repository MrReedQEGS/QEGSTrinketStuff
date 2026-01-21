#MPR- June 2024
#Python trinket turtle
import turtle,random
turtle.tracer(0, 0)
bob = turtle.Turtle()
bob.speed(0)
bob.hideturtle()
myCols = ((100,23,60),(0,100,100),(255,255,0),"black","white","brown",(23,17,192),(150,150,150),(56,56,56),(220,220,200))

def DrawHouse(houseX,houseY,size):
  #Draw the front of a house
  someFillCol = random.choice(myCols)
  bob.penup()
  bob.goto(houseX,houseY)
  bob.pendown()
  #Draw the main house shape
  bob.color(someFillCol)
  bob.fillcolor(someFillCol)  # filling in colour
  bob.begin_fill()
  bob.goto(houseX+size,houseY)
  bob.goto(houseX+size,houseY+size)
  bob.goto(houseX+size//2,+houseY+int(size*1.5))
  bob.goto(houseX,houseY+size)
  bob.goto(houseX,houseY)
  bob.end_fill()
  
  #Penup, move, pendown and draw windows
  windowSize = size//10
  windowX = houseX + windowSize
  
  numHigh = random.randint(1,5)
  
  for z in range(random.randint(1,3)):
    windowY = houseY + windowSize
    
    for p in range(numHigh):
      someWindowCol = random.choice(myCols)
      bob.color(someWindowCol)
      bob.fillcolor(someWindowCol)
      bob.penup()
      bob.goto(windowX,windowY)
      bob.pendown()
      bob.begin_fill()
      for _ in range(4):
        bob.forward(windowSize)
        bob.left(90)
      bob.end_fill()
      
      windowY = windowY + windowSize*2
    
    windowX = windowX + windowSize*2
      
  
#Draw a load of houses!!
yCoord = -100
for j in range(10):
  xCoord = -200

  for i in range(20-j):
    size= random.randint(15+(j*2),30+(j*2))
    DrawHouse(xCoord,-yCoord,size)
    
    xCoord = xCoord + size
    
  yCoord = yCoord + 30
  
turtle.update()
