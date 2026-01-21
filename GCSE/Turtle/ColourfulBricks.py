import turtle,random
bob = turtle.Turtle()
bob.speed(0)

myColours = ["red","green","blue","yellow","orange","black","white"]

#Draw a square
def MySquare():
  someColour = random.choice(myColours)
  bob.fillcolor(someColour)
  bob.begin_fill()
  for i in range(4):
    bob.forward(20)
    bob.left(90)
  bob.end_fill()

for i in range(10):
  MySquare()
  bob.forward(20)

bob.penup()
bob.goto(10,20)
bob.pendown()

for i in range(10):
  MySquare()
  bob.forward(20)
