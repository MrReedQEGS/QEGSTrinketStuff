#python turtle trinket
import turtle
bob = turtle.Turtle()
bob.speed(0)

wn = turtle.Screen() #instant
wn.tracer(0) #instant

for i in range(1000):
  bob.forward(i*5)
  bob.left(90)

wn.update() #instant
