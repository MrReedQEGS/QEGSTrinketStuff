import turtle,random
bob = turtle.Turtle()
bob.speed(0)
bob.tracer(0,0)

houseX = -150
houseY = -200
odd = True

def DrawBrick(x,y):
  colR = random.randint(0,255)
  colG = random.randint(0,255)
  colB = random.randint(0,255)
  bob.fillcolor(colR,colG,colB)
  bob.begin_fill()
  for i in range(2):
    bob.forward(x)
    bob.left(90)
    bob.forward(y)
    bob.left(90)
  bob.end_fill()
for j in range(40):
  bob.penup()
  bob.goto(houseX,houseY)
  bob.pendown()
  for i in range(15):
    DrawBrick(20,10)
    bob.forward(20)
  odd = not odd
  if(odd):
    houseX = houseX + 10
  else:
    houseX = houseX - 10
  
  houseY = houseY + 10

bob.update()
