#Written by Mr Reed - 27.6.22
#THIS PROGRAM WILL NOT LOAD REAL BITMAPS.  
#YOUR "BITMAPS" MUST BE FORMATTED EXACTLY AS IN THE EXAMPLES PROVIDED parrot.bmp box.bmp, burgertime.bmp, QR.bmp etc.

#Things you might want to change...
instantDrawing = False
outlineEachBox = True
drawOutline = True
drawColourList = False
imageTitle = "Mr Reed's pixel art!"
allowedFiles = ["myBitmap.bmp","parrot.bmp","burgerTime.bmp","QR.bmp","box.bmp"]

##################################################################################################
##################################################################################################
##################################################################################################
##################################################################################################
#DO NOT EDIT ANYTHING BELOW THIS LINE...
import turtle
#Set by the user later on
fileToDraw = ""

#controls the size of each pixel...loaded from image header as "pxsize"  :)
pixelSize = 20 

#turtle.colormode(255)  - This line is needed in some IDEs including "coding rooms" and "codio".

bob = turtle.Turtle()
bob.speed(0)

#You may need to edit the screen size
#to fit on your image and colour list.
screen = turtle.Screen()
screen.setup(800, 800)

#Hide the turtle so we can enjoy the artwork
bob.hideturtle()

#This variable is read from the image file header as "pix"
NumOfPixelsWide = 0

#Variables for top left corner of pixel image
topLeftX = -170
topLeftY = 150

#Array to store all colours in RGB format
#They are loaded from the image file header.
cols = []

#####################
#sub progs
#####################
def LoadColourList(fileDataList):
  global cols,NumOfPixelsWide,pixelSize
  
  imageList = []
  
  for line in fileDataList:
    if(str(line[0:3]) == "col"):
      line = line.replace(" ","")  #Get rid of any spaces in the colour definition.  They are not needed.
      colAsList = line.split(",")
      newCol = [colAsList[1],colAsList[2],colAsList[3],colAsList[4],colAsList[5].rstrip()]
      cols.append(newCol)
    elif(str(line[0:3])== "pix"):
      #get pix value
      lineAsList = line.split(",")
      NumOfPixelsWide = int(lineAsList[1].rstrip())
    elif(str(line[0:6])== "pxsize"):
      #get pixsize value
      lineAsList = line.split(",")
      pixelSize = int(lineAsList[1].rstrip())
    
    else:  
      #ignore comment lines
      if(line[0] != "#" and line[0] != "" and line[0] != "\n" ):
        #This must be part of our image
        imageList.append(line)
      
  return imageList

#Turn binary colour code into RGB tuple
def FindColourCode(someCol):
  bFoundIt = False
  for col in cols:
    code = col[0]
    answerR = int(col[2])
    answerG = int(col[3])
    answerB = int(col[4])
    if(code.upper() == someCol.upper()):
      return (answerR,answerG,answerB)
  if(bFoundIt != True):
    return "Error"

#Draw the colours and names/RGB at the side of the image
def DrawColours(theTurtle):
  theTurtle.penup()
  xStart = topLeftX + (NumOfPixelsWide+2)*pixelSize
  theTurtle.setpos(xStart,topLeftY)
  theTurtle.pendown()
  yOffset = 0
  for col in cols:
    DrawPixel(theTurtle,xStart,topLeftY+yOffset,pixelSize,col[0])
    yOffset = yOffset - pixelSize
    
    theTurtle.penup()
    theTurtle.setpos(xStart + 20,topLeftY + yOffset)
    theTurtle.pendown()
  
    theTurtle.fillcolor("black")
    style = ('Courier', pixelSize*0.7, 'italic')
    myString = "RGB({},{},{})".format(int(col[2]),int(col[3]),int(col[4]))
    theTurtle.write(col[0] + " " + col[1] + " " + myString,font=style)
    
#Draw one pixel in a paricular place
def DrawPixel(theTurtle,xLoc,yLoc,size,col):
  if(instantDrawing == False):
    turtle.tracer(0,0)
  
  theTurtle.penup()
  theTurtle.setpos(xLoc,yLoc)
  theTurtle.pendown()
  theCol = FindColourCode(col)
  if(col == "error"):
    return
  if(drawOutline == False):
    theTurtle.color(theCol)
    
  theTurtle.fillcolor(theCol)
  theTurtle.begin_fill()
  for i in range(4):
    theTurtle.forward(size)
    theTurtle.right(90)
  theTurtle.end_fill()
  
  if(instantDrawing == False):
    turtle.update()

def GetFileName():
  
  while(True):
    choices = []
    i = 1
    
    for fileN in allowedFiles:
      print("{} : {}".format(i,fileN))
      choices.append(str(i))
      i = i + 1
      
    print("")
    theChoice = input("Type the number of the file you want to draw: ")
    if(theChoice not in choices):
      print("Pick again...")
    else:
      return allowedFiles[int(theChoice)-1]
  
###############
#MAIN BODY
###############

fileToDraw = GetFileName()

#Load the image file into a list
f = open(fileToDraw,"r")
imageAsList=f.readlines()
f.close()

#Load the colour list - all colours are lines starting "col" in file header
imageWithoutComments = LoadColourList(imageAsList)

#Set the current pixel drawing location as the top left
xPos = topLeftX
yPos = topLeftY

#Write a title
bob.penup()
bob.setpos(xPos,yPos+20)
bob.pendown()
bob.write(imageTitle)

#Make instant drawing happen
if(instantDrawing == True):
  turtle.tracer(0, 0)

#Draw the colours and names down the right hand side
if(drawColourList == True):
  DrawColours(bob)

#NOW DRAW EACH PIXEL!!!

for line in imageWithoutComments:
  lineList = line.split(",")
  for colour in lineList:
    DrawPixel(bob,xPos,yPos,pixelSize,colour.rstrip())
    xPos = xPos + pixelSize
  yPos = yPos - pixelSize
  xPos = topLeftX
  if(instantDrawing == True):
    turtle.update()
