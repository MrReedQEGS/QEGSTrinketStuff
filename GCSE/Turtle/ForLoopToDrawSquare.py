#make a turtle
import turtle
bob = turtle.Turtle()

#Set the colour you want
bob.fillcolor("red")

#Start colouring in
bob.begin_fill()

#Do your drawing
for i in range(4):
  bob.forward(100)
  bob.left(90)
  
#Stop colouring in
bob.end_fill()
