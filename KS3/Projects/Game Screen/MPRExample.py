#Make a turtle
import turtle,random
bob = turtle.Turtle()
WHITE = (255,255,255)
BLACK = (0,0,0)
BACK_COL_BLUE = (96,218,228)
HIGHLIGHT_BROWN = (205,140,74)
LIGHT_BROWN = (187,128,68)
MED_BROWN = (165,113,60)
DARK_BROWN = (156,86,57)
GRASS = (46,204,112)
GRASS_HIGHLIGHT = (48,214,119)
DIRT = (186,128,66)
PLANT = (38,174,96)

turtle.Screen().bgcolor(BACK_COL_BLUE)
bob.speed(0)

def DrawRect(x,y,xSize,ySize,col,colOutline,rounded=False):
  #rounded corners can be on or off
  bob.penup()
  bob.setpos(x,y)
  bob.pendown()
  bob.color(colOutline)
  bob.fillcolor(col)
  bob.begin_fill()
  
  if(rounded == False):
    for i in range(2):
      bob.forward(xSize)
      bob.left(90)
      bob.forward(ySize)
      bob.left(90)
  else:
    for i in range(2):
      bob.forward(xSize-3)
      bob.circle(3,90)
      bob.forward(ySize-3)
      bob.circle(3,90)
      
  bob.end_fill()

def DrawPlant(x,y,col):
  bob.penup()
  bob.setpos(x,y)
  bob.pendown()
  bob.color(col)
  bob.fillcolor(col)
  bob.begin_fill()
  bob.setpos(x-15,y+5)
  bob.setpos(x-5,y+10)
  bob.setpos(x-9,y+18)
  bob.setpos(x,y+15)
  bob.setpos(x+5,y+25)
  bob.setpos(x+9,y+10)
  bob.setpos(x+14,y+8)
  bob.setpos(x+10,y)
  bob.setpos(x,y)
  bob.end_fill()

def DrawTriangle(x,y,col):
  #rounded corners can be on or off
  bob.penup()
  bob.setpos(x,y)
  bob.pendown()
  bob.color(col)
  bob.fillcolor(col)

  bob.begin_fill()
  bob.setheading(0)
  bob.setpos(x+30,y)
  bob.setpos(x+15,y+15)
  bob.setpos(x,y)
  bob.end_fill()

def DrawText(x,y,theText):
  bob.penup()
  bob.setpos(x,y)
  bob.pendown()
  bob.color(BLACK)
  bob.write(theText)

def DrawCrate(x,y):
  DrawRect(x,y,100,100,LIGHT_BROWN,MED_BROWN,True)
  DrawRect(x+15,y+15,70,70,MED_BROWN,MED_BROWN,True)
  DrawRect(x+22,y+22,10,10,DARK_BROWN,DARK_BROWN,True)
  DrawRect(x+68,y+22,10,10,DARK_BROWN,DARK_BROWN,True)
  DrawRect(x+68,y+68,10,10,DARK_BROWN,DARK_BROWN,True)
  DrawRect(x+22,y+68,10,10,DARK_BROWN,DARK_BROWN,True)
  DrawRect(x+14,y+14,71,2,HIGHLIGHT_BROWN,HIGHLIGHT_BROWN)
  DrawRect(x+12,y+14,2,73,HIGHLIGHT_BROWN,HIGHLIGHT_BROWN)
  
def DrawGrass():
  DrawRect(-300,-200,600,30,GRASS,GRASS)
  DrawRect(-300,-170,600,2,GRASS_HIGHLIGHT,GRASS_HIGHLIGHT)
  for i in range(14):
    DrawTriangle(-200+i*30,-200,DIRT)
  
#Main
DrawPlant(-120,-172,PLANT)
DrawCrate(-100,-170)
DrawCrate(3,-170)
DrawCrate(-51.5,-67)
DrawGrass()
DrawText(60,150,"HI SCORE : 0")
DrawText(60,135,"SCORE    : 0")
bob.hideturtle()
