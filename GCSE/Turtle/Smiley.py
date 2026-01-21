#python turtle trinket
#make a turtle
import turtle
bob = turtle.Turtle()
bob.speed(0)
#rgb colour picker
bob.fillcolor("yellow")
bob.begin_fill()
bob.circle(80)
bob.end_fill()

bob.fillcolor("black")
bob.penup() #eye 1
bob.goto(30,80)
bob.pendown()
bob.begin_fill() 
bob.circle(20)
bob.end_fill()

bob.penup() #eye 2
bob.goto(-30,80)
bob.pendown()
bob.begin_fill()
bob.circle(20)
bob.end_fill()

bob.penup()  #mouth
bob.goto(-26,40)
bob.pendown()
bob.right(90)
bob.circle(25,180)
bob.hideturtle()
    
