#Empire State Building

import turtle
bob = turtle.Turtle()
bob.speed(0)

instantDrawing = True
if (instantDrawing):
  bob.tracer(0,0)


#WINDOW CODE DO NOT DELETE!!!
WindowSize = 3.5
WindowGap = WindowSize + 2


def DrawSquare(sizeOfSquare):
  for i in range(4):
      bob.color("yellow")
      bob.forward(sizeOfSquare)
      bob.left(90)

def DrawColOfWindows(heightOfCol):
  for j in range(heightOfCol):
    DrawSquare(WindowSize)
    bob.penup()
    bob.left(90)
    bob.forward(WindowGap)
    bob.right(90)
    bob.pendown()
#
drawingArea = turtle.Screen()
drawingArea.setup(width = 450,height = 700)
#


#MAIN CODE


#bottom left positioning
bob.penup()
bob.backward(100)
bob.right(90)
bob.forward(200)
bob.pendown()
bob.left(90)
bob.pendown()

#Basic rectangular outline of the Empire state building 


bob.color("red")
bob.begin_fill()
bob.fillcolor("black")
bob.forward(200)
bob.left(90)
bob.forward(500)
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(500)
bob.end_fill()

#Start of the full outline
bob.color("white")
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(40)
bob.left(90)
bob.forward(200)
bob.left(90)
bob.forward(40)
#
#
bob.left(90)
bob.left(90)
bob.penup()
bob.forward(40)
bob.right(90)
bob.pendown()
bob.forward(20)
bob.left(90)
#Make line below same as long line 1 & 2
bob.forward(190)
#Make line above same as long line 1 & 2
bob.right(90)
bob.penup()
bob.forward(160)
bob.right(90)
bob.pendown()
#long line 1
bob.forward(190)
#long line 2
bob.right(90)
bob.right(90)
bob.forward(190)
bob.left(90)
bob.forward(10)
#
#
bob.right(90)
bob.forward(65)
bob.left(90)
#
#
bob.forward(5)
bob.right(90)
bob.forward(30)
#
bob.left(90)
bob.forward(2.5)
bob.right(90)
bob.forward(15)
bob.left(90)
#
bob.forward(122.5)
bob.left(90)
bob.forward(15)
#
bob.right(90)
bob.forward(2.5)
#
bob.left(90)
bob.forward(30)
bob.right(90)
bob.forward(5)
bob.left(90)
bob.forward(65)
#
bob.right(90)
bob.forward(12)
#
bob.hideturtle()
#window idea



#window
#if (instantDrawing):
#  bob.tracer(0,0)
#Window column 1
bob.penup()
bob.goto(-95,-160)
bob.pendown()

DrawColOfWindows(7)


#Window column 2
bob.penup()
bob.goto(-90,-160)
bob.pendown()

DrawColOfWindows(7)


#Window column 3
bob.penup()
bob.goto(-85,-160)
bob.pendown()

DrawColOfWindows(7)

#Window column 4
bob.penup()
bob.goto(-80,-160)
bob.pendown()

DrawColOfWindows(7)


#Window column 5
bob.penup()
bob.goto(-75,27)
bob.pendown()

DrawColOfWindows(41)


#Window column 6
bob.penup()
bob.goto(-70,27)
bob.pendown()

DrawColOfWindows(41)


#Window column 7
bob.penup()
bob.goto(-63,93)
bob.pendown()

DrawColOfWindows(53)


#Window column 8
bob.penup()
bob.goto(-58,122)
bob.pendown()

DrawColOfWindows(58)


#Window column 9
bob.penup()
bob.goto(-53,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 10
bob.penup()
bob.goto(-48,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 11
bob.penup()
bob.goto(-43,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 12
bob.penup()
bob.goto(-38,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 13
bob.penup()
bob.goto(-33,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 14
bob.penup()
bob.goto(-28,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 15
bob.penup()
bob.goto(-23,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 16
bob.penup()
bob.goto(-18,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 17
bob.penup()
bob.goto(-13,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 18
bob.penup()
bob.goto(-8,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 19
bob.penup()
bob.goto(-3,138)
bob.pendown()

DrawColOfWindows(61)


#Window column 20
bob.penup()
bob.goto(2,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 21
bob.penup()
bob.goto(7,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 22
bob.penup()
bob.goto(12,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 23
bob.penup()
bob.goto(17,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 24
bob.penup()
bob.goto(22,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 25
bob.penup()
bob.goto(27,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 26
bob.penup()
bob.goto(32,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 27
bob.penup()
bob.goto(37,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 28
bob.penup()
bob.goto(42,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 29
bob.penup()
bob.goto(47,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 30
bob.penup()
bob.goto(52,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 31
bob.penup()
bob.goto(57,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 33
bob.penup()
bob.goto(62,138)
bob.pendown()

DrawColOfWindows(61)

#Window column 34
bob.penup()
bob.goto(65,122)
bob.pendown()

DrawColOfWindows(58)

#Window column 35
bob.penup()
bob.goto(69,94)
bob.pendown()

DrawColOfWindows(53)


#Window column 36
bob.penup()
bob.goto(72,28)
bob.pendown()

DrawColOfWindows(41)

#Window column 36
bob.penup()
bob.goto(77,28)
bob.pendown()

DrawColOfWindows(41)

#Window column 39
bob.penup()
bob.goto(82,-159)
bob.pendown()

DrawColOfWindows(7)

#Window column 40
bob.penup()
bob.goto(87,-159)
bob.pendown()

DrawColOfWindows(7)

#Window column 41
bob.penup()
bob.goto(92,-159)
bob.pendown()

DrawColOfWindows(7)

#Window column 42
bob.penup()
bob.goto(97,-159)
bob.pendown()

DrawColOfWindows(7)
#
#
#
#bob.penup()
#
#
bob.penup()
bob.pencolor("red")
bob.right(90)
bob.forward(337)
bob.left(90)
bob.forward(38)
bob.pendown()
#
#
bob.pencolor("grey")
bob.begin_fill()
bob.fillcolor("grey")
bob.forward(20)
bob.forward(41.25)
bob.right(90)
bob.forward(150)
#reverse
bob.back(150)
bob.left(90)
bob.back(41.25)
bob.penup()
bob.goto(-2,240)
bob.pendown()
bob.goto(41.25,140)
#
bob.penup()
bob.goto(-2,240)
bob.pendown()
#
bob.goto(-40,140)
bob.goto(41.25,140)
bob.end_fill()


bob.penup()
if (instantDrawing):
  bob.update()
bob.pendown()
