#Written by Mr Reed - 1.7.22
#An attempt to make random NFT style images that are all slightly different.

import turtle, random
#image grid defaults
GRID_WIDTH = 5
GRID_HEIGHT = 15

#Image name
MAIN_IMAGE = "bird.bmp"
fileToDraw = MAIN_IMAGE
BIT_DEPTH = 4

#Extras?
drawGlassesForThisShape = False
drawHairForThisShape = False
drawBrowsForThisShape = False

#mask for transparency
mask = "x"*BIT_DEPTH

#controls the size of each pixel...loaded from image header as "pxsize"  :)
pixelSize = 0 

#Toggle this to make the drawing happen instantly!
instantDrawing = True

showColList = False

bob = turtle.Turtle()
bob.speed(0)

#You may need to edit the screen size
#to fit on your image and colour list.
screen = turtle.Screen()
screen.setup(1000, 1000)

#Hide the turtle so we can enjoy the artwork
bob.hideturtle()

#This variable is read from the image file header as "pix"
NumOfPixelsWide = 0

#Pixel borders are optional
drawOutline = False

#Variables for top left corner of pixel image
topLeftOfWholeDrawingX = -220
topLeftOfWholeDrawingY = 350

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

#ZFill the binary number to make the number codes the correct
#length
def MyFill(someString,fillSize):
  while(len(someString) <fillSize):
    someString = "0" + someString
  return someString

def RandomiseCols():
  #Change the colour array to new random RGB cols.
  global cols
  numOfCols = len(cols)
  cols = []
  for i in range(numOfCols):
    RandomR = random.randint(0,255)
    RandomG = random.randint(0,255)
    RandomB = random.randint(0,255)
    
    binNum = str(bin(i))[2:]
    binNum = MyFill(binNum,BIT_DEPTH)
    
    cols.append([binNum,"notneeded",RandomR,RandomG,RandomB])

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

#Draw one pixel in a paricular place
def DrawPixel(theTurtle,xLoc,yLoc,size,col):
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

def DrawThing(someImageList):
  global xPos
  global yPos
  for line in someImageList:
      lineList = line.split(",")
      for colour in lineList:
        
        if(colour.rstrip() != mask):
          DrawPixel(bob,xPos,yPos,pixelSize,colour.rstrip())
        
        xPos = xPos + pixelSize
      yPos = yPos - pixelSize
      xPos = topLeftOfThisImageX + ((NumOfPixelsWide + 1)*j*pixelSize)

def DrawGlasses():
  if(drawGlassesForThisShape != True):
    return
  someInt = random.randint(1,10)
  if(someInt > 7):
    DrawThing(glassesImageList1)
    
def DrawHair():
  if(drawHairForThisShape != True):
    return
  someInt = random.randint(1,10)
  if(someInt >= 5):
    DrawThing(hairImageList)
    
def DrawBrows():
  if(drawBrowsForThisShape != True):
    return
  someInt = random.randint(1,10)
  if(someInt > 6):
    DrawThing(browsImageList)
  
###############
#MAIN BODY
###############

#Load the image file into a list
f = open(fileToDraw,"r")
imageAsList=f.readlines()
f.close()

glassesFile = open("glasses1.bmp","r")
glassesImageList1=glassesFile.readlines()
glassesFile.close()

hairFile = open("hair.bmp","r")
hairImageList=hairFile.readlines()
hairFile.close()

browsFile = open("brows.bmp","r")
browsImageList=browsFile.readlines()
browsFile.close()

#Load the colour list - all colours are lines starting "col" in file header
imageWithoutComments = LoadColourList(imageAsList)

#Set the current pixel drawing location as the top left
topLeftOfThisImageX = topLeftOfWholeDrawingX
topLeftOfThisImageY = topLeftOfWholeDrawingY

#Make instant drawing happen
if(instantDrawing == True):
  turtle.tracer(0, 0)

#Draw the bitmap several times in different colours
for x in range(GRID_HEIGHT):
  
  for j in range(GRID_WIDTH):
    
    RandomiseCols()
    originalXPos = topLeftOfThisImageX + ((NumOfPixelsWide + 1)*j*pixelSize)
    originalYPos = topLeftOfThisImageY - ((23 + 1)*x*pixelSize)
    xPos = originalXPos
    yPos = originalYPos
   
    DrawThing(imageWithoutComments)
    
    xPos = originalXPos
    yPos = originalYPos
    DrawGlasses()
    
    xPos = originalXPos
    yPos = originalYPos
    DrawHair()
    
    xPos = originalXPos
    yPos = originalYPos
    DrawBrows()
    
if(instantDrawing == True):
  turtle.update()

