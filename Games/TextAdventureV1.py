# Mr Reed
# October 2021
# An attempt at a text adventure game!

#BorderCharacters :)
#╚ ╔ ╩ ╦ ╠ ═ ╬ ╣║ ╗╝

#IMPORTS
import sys
import time
import os
import random
import datetime

#clear = lambda: os.system('clear')

someWords = []

testing = False
combosMade = 0

class ComboObject:
  def __init__(self, comboItemList,resultItemList,successMessage):
    self.comboItemList = comboItemList
    self.resultItemList = resultItemList #max 2 items in this list
    self.successMessage = successMessage

class GameObject:
  def __init__(self, imageList, name, colour):
        self.imageList = imageList
        self.name = name
        self.colour = colour
        
class LocationObject:
  def __init__(self,num,name,image,description,extraDescription,locationItems,extraItems,loadingTime,locationLoadingMessage=""):
        self.num = num
        self.name = name
        self.image = image
        self.description = description
        self.extraDescription = extraDescription
        self.locationItems = locationItems
        #have I dealt with extra look items such as the rat?
        self.extraItems = extraItems
        self.beenBefore = False
        self.locationLoadingMessage = locationLoadingMessage
        self.loadingTime = loadingTime

NiceThingsAboutMe = ["MR REED IS THE BEST TEACHER",
                    "MR REED IS GOOD AT CODING",
                    "MR REED IS GOOD AT PROGRAMMING",
                    "MR REED IS A GOOD PROGRAMMER",
                    "MR REED IS AN AMAZING TEACHER",
                    "MR REED IS AMAZING",
                    "MR REED IS AWESOME",
                    "MR REED IS MODEST",
                    "MR REED IS A LEGEND"]
   
#Colour CONSTANTS
END='\033[0m'
Bold='\033[01m'
Italic = '\033[03m'
Underline='\033[04m'
Strikethrough='\033[09m'

Blink    = '\33[5m'
Blink2   = '\33[6m'
Black='\033[30m'
Red='\033[31m'
Green='\033[0;32m'
Yellow='\033[33m'
Blue='\033[34m'
Purple='\033[35m'
Cyan='\033[36m'
White="\033[0;37m"      

BlackBG='\033[40m'
RedBG='\033[41m'
GreenBG='\033[42m'
YellowBG='\033[43m'
BlueBG='\033[44m'
PurpleBG='\033[45m'
CyanBG='\033[46m'

#END ="\033[0m" # End formatting
#Black="\033[0;30m"        # Black
#Red="\033[0;31m"          # Red
#Green="\033[0;32m"        # Green
#Yellow="\033[0;33m"       # Yellow
#Blue="\033[0;34m"         # Blue
#Purple="\033[0;35m"       # Purple
#Cyan="\033[0;36m"         # Cyan
#White="\033[0;37m"        # White

playerName = "None"
startType = "None"
startLevel = "None"

chaliceFound = False
chaliceSafe = False
mrBeckerQuizDone = False
timesQuizSaid = 0

#Inventory items
playerInventorySlots = 4
invLines = 6
roomTitleColour = Blue
menuColour = Blue
quitPageColour = Blue

keyImageList = [
"            ",
" ,o.    8 8 ",
"d   bzza8o8b",
" `o'        ",
"            ",
"    Key     "]
        

ratImageList = [
"    ()()    ",     
"    (..)    ",   
"    /\/\    ",    
"   c\db/o   ",
"            ",
"    Rat     "]

fatRatImageList = [
"  _()_()_   ",     
" (   ..  )  ",   
" /   \/  \  ",    
" |   ||   | ",
" C\__db__/D ",
"  Fat Rat   "]

cheeseImageList = [
"     ____   ",
"    /|o  |  ",
"   /o|  o|  ",
"  /o_|_o_|  ",
"            ",
"   Cheese   "]

pantsImageList = [
",==========,",
"|   |  |   |",
"`-./    \.-'",
"   `.__.'   ",
"            ",
"   Pants    "]

anchorImageList = [
"            ",
"    -+-     ",
"   ^ | ^    ",
"   \_|_/    ",
"            ",
" Tiny Anchor"]

chaliceImageList = [
"  \=======/ ",
"   \     /  ",
"    \(+)/   ",
"     ) (    ",
"  --'---`-- ",
"   Chalice  "]

nothingImageList = [
"            ",
"            ",
"   Empty    ",
"            ",
"            ",
"            "]

toyBoatImageList = [
"    /|      ",
"   / |      ",          
"  /__|__    ",
"\--------/  ",
" `~~~~~~'   ",
"Broken Boat "]

toyBoatFixedImageList = [
"    /|  -+- ",
"   / | ^ | ^",          
"  /__|_\_|_/",
"\--------/  ",
" `~~~~~~'   ",
" Fixed Boat "]

caveTrollImageList = [
"   (*_*)    ",
" ___\w/___  ",
"(|_ ~~~ _|) ",
"   |___|    ",
"  /_/ \_\   ",
" Cave troll "]

#for beckers calculator!!!
randomCode = random.randint(40000,50000)
  
calcImageList = [
" ---------- ",
''' |  '''+str(randomCode)+''' | ''',
" |+ . . . | ",
" |- . . = | ",
" ---------- ",
" Calculator "
  ]
  
tinyKettleBellImageList = [
"     _      ",
"    | |     ",
"   /|_|\    ",
"  |     |   ",
"   \___/    ",
" Kettle Bell"
  ]
  
brokenGuitarImageList = [
"   #|| |     ",
"    || |     ",
"   /|| |\    ",
"  | (__) |   ",
"   \____/    ",
"Broken Guitar"
  ]

fixedGuitarImageList = [
"   #||||#    ",
"    ||||     ",
"   /||||\    ",
"  | (__) |   ",
"   \____/    ",
" Fixed Guitar"
  ]

guitarStringImageList = [
"  -.         ",
"    `\       ",
"      ~.     ",
"        )    ",
"        (    ",
"Guitar String"
  ]

inventoryBox = [
"----------------",
"|"
]

def WrapInInventoryBox(someItem):
  #Game objects are 6 lines of text, so 8 with a box around them
  someImageList = someItem.imageList
  theColour = someItem.colour
  #put a box around it using inventoryBox
  #[0] is for top and bottom
  #[1] is for left and right sides
  top = inventoryBox[0] 
  side = inventoryBox[1]
  newList = []
  newList.append(top)
  
  for line in someImageList:
    newLine = side + " " + theColour + line + " " + END + side
    newList.append(newLine)
    
  newList.append(top)
  
  return newList

#test = WrapInInventoryBox(pantsImageList)

#create the game objects
keyObject = GameObject(keyImageList,"key",Red)
ratObject = GameObject(ratImageList,"rat",Blue)
cheeseObject = GameObject(cheeseImageList,"cheese",Green)
pantsObject = GameObject(pantsImageList,"pants",Purple)
anchorObject = GameObject(anchorImageList,"tiny anchor",Black)
calcObject = GameObject(calcImageList,"calculator",Blue)
chaliceObject = GameObject(chaliceImageList,"chalice",Green)
nothingObject = GameObject(nothingImageList,"nothing",Black)
fatRatObject = GameObject(fatRatImageList,"fat rat",Blue)
toyBoatObject = GameObject(toyBoatImageList,"broken boat",Green)
toyBoatFixedObject = GameObject(toyBoatFixedImageList,"fixed boat",Green)
caveTrollObject = GameObject(caveTrollImageList,"cave troll",Red)
kettleBelleObject = GameObject(tinyKettleBellImageList,"kettle bell",Blue)
brokenGuitarObject = GameObject(brokenGuitarImageList,"broken guitar",Red)
fixedGuitarObject = GameObject(fixedGuitarImageList,"fixed guitar",Red)
guitarStringObject = GameObject(guitarStringImageList,"guitar string",Green)


#fill up the inventory with nothing so it displays properly even when empty.
inventory = []
for i in range(playerInventorySlots):
  inventory.append(nothingObject)

fatRatCombo = ComboObject([ratObject,cheeseObject],[fatRatObject],"Combo correct!!! A well fed fat rat was added to your inventory!")
boatCombo = ComboObject([anchorObject,toyBoatObject],[toyBoatFixedObject],"Combo correct!!! You fixed the little boat and it is now in your inventory!")
guitarCombo = ComboObject([guitarStringObject,brokenGuitarObject],[fixedGuitarObject],"Combo correct!!! The guitar now has all strings and is ready to rock...it is in your inventory.")

comboList = [fatRatCombo,boatCombo,guitarCombo]

#SECRETS
class Secret:
  def __init__(self, clue, achievedString, foundString):
        self.clue = clue
        self.achievedString = achievedString
        self.foundString = foundString
        self.achieved = False

secret1 = Secret("Say something nice about the game designer.","Mr Reed is indeed an amazing and modest man!!!!","Indeed he is!  A point well made...secret unlocked!")
secret2 = Secret("Not all things should be dropped!","Thanks for staying fully dressed!","That would indeed be rude...secret unlocked!")
secret3 = Secret("Do not try to go where E.T. tried to phone!","Going home is for wimps...keep adventuring!","Absolutely not, going home is for wimps!...secret unlocked!")
secret4 = Secret("It is nice to find out about things.","Do you recognise that ASCII photo?","Good looking teacher alert...secret unlocked!")
secret5 = Secret("Seen that menu a few times now.","Spammed the menu with style.  Well done.","Stop doing that!!!...secret unlocked!")
secret6 = Secret("Be impressed by what he has achieved!","Keep trying and one day you may beat Mr Reed's high score.","One day you could be as good as Mr Reed...secret unlocked!")
secret7 = Secret("Changed your mind?","Quitting is for wimps!!!","Make your mind up.  Quit, don't quit.  Which one is it?...secret unlocked!")
secret8 = Secret("It's a dangerous business...going out of your door.","You stayed in the same place!","Not a brave bone in your body.Too scared to move???...secret unlocked!")
secret9 = Secret("Why no moniker?","A nameless adventurer is of no use to anyone!","Are you afraid you will fail? Give a name so all can remember you...secret unlocked!")
secret10 = Secret("Off we go again.","You quit, but then went back for more adventuring.","Welcome back...secret unlocked!")
secret11 = Secret("Set it free.","Returned the fat rat to nature.","The Gloomy Forest is a scary place even for a fat rat. He quicky runs away...secret unlocked!")
secret12 = Secret("Salutations to the puzzle keeper.","You said hello to Mr Becker!","He acknowledges you with a stange look...secret unlocked!")
secret13 = Secret("A pityful man with hidden treasures!","Chalice located!!!!!!!","Despite Mr Becker, a most amazing artifact has been found...secret unlocked!")
secret14 = Secret("You really wanna do that quiz.","You found the hidden maths quiz.","You kept trying and the most amazing quiz is your prize...secret unlocked!")
secret15 = Secret("Do not try to be him!","You tried to be Mr Reed...and failed.","That name is reserved for the most amazing and modest of adventurers.  You cannot be him!...secret unlocked!")
secret16 = Secret("The secret quiz was no match for me!!!","Has anyone checked in on Mr Becker recently?","The not so secret quiz was actually quite easy...secret unlocked!")
secret17 = Secret("It is not all about winning.","Quiz purposely failed so Mr Becker feels less sad.","It is the taking part that counts...secret unlocked!")
secret18 = Secret("Get crafting.","You went crafting and it was good.","Combos are fun, there are lots more to find....secret unlocked!")
secret19 = Secret("Find the troll a forever home.","Cave trolls love caves...simples!","The troll loves his new home.  He immediately craws between the rubble never to be seen again....secret unlocked!")

secretsList = [secret1,secret2,secret3,secret4,secret5,
               secret6,secret7,secret8,secret9,secret10,
               secret11,secret12,secret13,secret14,secret15,
               secret16,secret17,secret18,secret19
               ]

#https://textart.sh/
darkCaveImage = '''

▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒
▒▒▒▒▒▒░░▒▒░░░░▓▓▒▒░░▒▒▒▒░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒
▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░
▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██████▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒░░
░░░░▒▒▒▒▒▒░░░░▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒████████▓▓██▓▓▓▓██▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░▒▒░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒██████████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒██████████████▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▒▒▓▓████████▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒██████████▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓████▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░▒▒▒▒▓▓▓▓▓▓████▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓██▓▓████▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒██▓▓▓▓▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓██████▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓████▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▒▒░░░░▒▒░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒▓▓██████▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░░░
░░░░░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▓▓▒▒▒▒▓▓▓▓▓▓████▓▓████░░░░░░░░░░░░░░░░░░░░░░░░
░░▒▒░░░░▒▒▒▒░░░░░░░░▒▒▒▒▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓██████▓▓██▓▓░░░░░░░░░░░░░░░░░░░░░░
░░▒▒░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓██▓▓██████▓▓▓▓██░░░░░░░░░░░░░░░░░░░░░░
░░▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▒▒▓▓▒▒▓▓▒▒▓▓▓▓▓▓██████▓▓▓▓██░░▒▒░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓████████████▒▒▒▒░░░░░░░░░░░░░░░░░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒██▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓▒▒▓▓▓▓██████████████▓▓░░░░░░░░░░░░░░░░░░
▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████▓▓▓▓▓▓▓▓▓▓██████████████░░░░░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████████████████████████████████████████████████████████████████████▓▓░░░░░░░░░░░░░░░░
██████████████▓▓████▓▓████▓▓██████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░▒▒▒▒░░▒▒
▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░'''

gloomyForestImage = '''

▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒░░▒▒░░░░░░▒▒▓▓▒▒░░▒▒▒▒░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▓▓▓▓▓▓██▓▓██▓▓██████▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒░░░░░░▒▒▓▓░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓
▓▓░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒▓▓▒▒░░▒▒▒▒░░▓▓░░▒▒▒▒▓▓▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░▒▒░░▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒
██▓▓▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓██▓▓▓▓██▓▓▓▓██▒▒░░▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒░░▓▓▒▒░░▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░
██▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒▒▒░░░░░░░░░░▒▒▓▓░░░░░░░░░░░░░░▒▒▒▒░░░░▒▒▒▒░░▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒░░▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒░░▒▒▓▓░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒
▓▓▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▓▓████▓▓▓▓▓▓▓▓▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░▒▒░░▒▒▒▒░░░░░░░░▒▒░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░▓▓▒▒▓▓▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▒▒░░▒▒░░░░▒▒▒▒░░▒▒░░
▒▒░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██▓▓██▓▓▓▓██▒▒░░░░░░░░▒▒░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒░░▒▒░░░░
░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓██▓▓████▓▓▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒░░░░▒▒░░░░░░░░░░░░░░░░
░░▒▒░░▓▓░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓▓▓██▓▓▓▓████▓▓██▒▒▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░
░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓██▓▓██▓▓██▓▓▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▒▒▒▒▓▓▒▒▓▓░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒
▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░▒▒▓▓▓▓██▓▓▓▓██▓▓██████▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒░░▒▒░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒
▒▒▒▒▒▒░░▒▒░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██▓▓▓▓▓▓▓▓██████▒▒░░▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░░░░░░░░░▒▒░░▒▒░░░░░░▒▒░░▒▒▓▓▒▒▒▒░░░░▒▒▒▒▓▓▓▓▒▒▓▓▒▒▓▓▒▒██▓▓▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓██▒▒░░▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░░░▒▒░░▒▒░░▒▒░░▒▒▒▒
▒▒░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓██████▓▓▓▓▓▓██▓▓██▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▓▓▒▒▓▓▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒░░░░░░▒▒░░░░▒▒░░▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒░░▓▓▓▓▓▓████▓▓▓▓▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓██▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒
▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒▒▒▓▓██▓▓██▓▓██▓▓████████▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▓▓░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░
▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░▒▒████▓▓██▓▓██▓▓██████▓▓██░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▓▓▓▓░░░░░░░░░░░░▒▒▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▓▓▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓██▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░░░░░
▓▓▒▒▒▒▒▒░░░░░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓▓▓██████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒░░░░░░░░░░▒▒██▒▒▒▒░░░░▒▒▒▒▒▒░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓████████▓▓▓▓▒▒▒▒▓▓██▓▓▓▓▓▓▒▒░░░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒
▓▓▒▒▒▒▒▒░░░░░░░░░░▓▓▓▓▓▓██▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓████░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░▒▒░░▓▓▓▓▒▒░░▒▒░░░░░░░░▓▓▓▓▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒░░▒▒▓▓▒▒▓▓██▒▒▒▒░░▒▒░░▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒
▓▓▓▓▒▒▒▒░░░░░░░░▓▓▓▓██▓▓▓▓██████████████▓▓▓▓██▓▓░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▓▓░░░░▒▒░░░░░░▒▒░░▓▓▒▒▓▓▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒██▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓░░▒▒░░░░▒▒▒▒▒▒▓▓▒▒░░▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓
▓▓██▓▓▒▒░░░░░░▓▓▓▓██▓▓▓▓▓▓██▓▓██▓▓▓▓▓▓▓▓██▓▓▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▓▓░░░░▒▒▒▒▒▒░░░░░░▓▓▓▓▒▒░░▒▒▓▓▓▓▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒░░░░░░▒▒▓▓▓▓▒▒▓▓▓▓██████▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓██▓▓░░▒▒▓▓▓▓██▓▓██▓▓████▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░▒▒░░░░▒▒░░▒▒▒▒░░░░░░▒▒▒▒██▒▒▒▒░░▒▒░░▒▒░░▓▓▓▓░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░▒▒▒▒░░░░▒▒▓▓▒▒▓▓██▓▓▒▒░░░░░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒░░▒▒▒▒░░░░▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░
████▓▓▓▓▒▒▓▓██▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓████▓▓██▓▓██▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▓▓░░▒▒▒▒▒▒▒▒░░░░▒▒▓▓▒▒▓▓▓▓▓▓░░▒▒▒▒▓▓▒▒▒▒░░▒▒░░░░░░▒▒░░▓▓████▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██▓▓▒▒██▓▓████████▓▓██████▓▓██████▓▓██▓▓██▓▓▓▓▒▒░░░░░░▒▒░░▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██▒▒▒▒░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▓▓██▓▓▒▒░░▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██▓▓████▓▓▓▓▓▓██▓▓▓▓▓▓▓▓████▒▒░░▒▒░░▒▒▒▒░░░░░░▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░▒▒░░▒▒░░░░▓▓██▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒
▓▓▓▓▓▓████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓▓▓██▓▓▓▓██████▓▓░░░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓░░░░░░▓▓▒▒▒▒██▒▒██░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓██▒▒░░░░░░▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░░░▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░░░░░▒▒▒▒░░░░░░▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒░░
▓▓██▓▓██▓▓▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▓▓██▓▓██████▓▓██▓▓░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░░░▒▒▓▓▒▒░░░░░░░░▒▒▒▒░░░░░░▒▒▓▓▓▓░░▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░░░░░▒▒░░░░▒▒░░▒▒▒▒▓▓▒▒▓▓▒▒░░░░░░▒▒▓▓▓▓▒▒░░░░░░░░▓▓▒▒░░░░░░▒▒░░▒▒▒▒░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒
██▓▓██▓▓▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓██▓▓████████▓▓░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░▒▒▓▓▒▒░░░░▒▒▒▒▓▓▓▓██▓▓██▓▓██▓▓▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▓▓░░░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒▓▓▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒░░
▓▓▓▓▓▓▒▒▓▓▒▒▓▓██▓▓▓▓██▓▓▓▓██████████▓▓████▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓░░▒▒██▓▓▓▓▒▒▓▓██████████▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒
▓▓▓▓▓▓██▒▒▓▓██▓▓▓▓████████████▓▓██▓▓██▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▒▒▓▓▒▒░░▒▒▓▓████▓▓░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▒▒░░▒▒▒▒░░▒▒░░░░▓▓▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒░░░░░░░░░░▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒░░
▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓██████████▓▓▓▓████▓▓▓▓▓▓▓▓████▓▓▓▓██▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓██▓▓▒▒░░▒▒░░░░░░▒▒▒▒░░▒▒▒▒▒▒██████████▓▓▓▓▓▓██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▓▓▓▓▓▓▒▒▓▓▒▒░░░░▒▒▒▒░░░░░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░
▓▓▓▓▓▓▒▒▓▓██▓▓██▓▓██▓▓▓▓██████████▓▓██████▓▓████████████▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓██▒▒░░▒▒░░░░▓▓░░▒▒▒▒░░▒▒▓▓▓▓██▓▓░░▒▒▒▒▓▓██░░░░▒▒░░▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒░░▒▒▒▒▓▓▓▓▒▒░░░░▒▒▒▒░░░░░░░░▒▒░░░░▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░░░
▓▓▓▓▓▓▓▓████▓▓▓▓▓▓██▓▓████████████▓▓████▓▓██████████████████▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓████████▓▓▓▓████▓▓▓▓██▓▓██████▒▒▒▒▒▒▒▒░░░░██▒▒░░░░▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓░░░░░░▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒░░░░▒▒░░░░░░░░▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒
██▓▓██████▓▓██████████████████████████████▓▓██████████████████▓▓████▓▓██▓▓▓▓▓▓▓▓██████████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██▓▓████████████████▓▓▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒██░░░░░░▒▒▒▒▒▒▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒░░▒▒░░░░░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▓▓▓▓██▓▓▓▓██████▓▓████████████████████████████████████████████████████▓▓██████▓▓████████████▓▓▓▓▓▓▓▓▓▓▓▓████▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒██▓▓▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒██▓▓▓▓▓▓▓▓▓▓██████▓▓▓▓▒▒▒▒▓▓▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒░░
▓▓▓▓▓▓▓▓▓▓██▓▓▓▓████████████▓▓██████████████████████████████▓▓██████████▓▓▓▓██▓▓██▓▓████████████████████▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒██▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒░░▒▒▓▓▓▓▒▒▒▒░░▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░░░
██▓▓▓▓▓▓▓▓████████████████████████▓▓██████████████████████████████████████████▓▓██▓▓████████████████▓▓▒▒▒▒▒▒░░░░▒▒▒▒░░░░▒▒▒▒▒▒░░▓▓██░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░▒▒░░░░▒▒░░░░▒▒░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░░░░░░░░░
██▓▓▓▓▓▓██▓▓████████████████████████▓▓████████████████████████████████████▓▓████████████████████▓▓▓▓▒▒▓▓░░░░▒▒▒▒░░░░░░░░▒▒▒▒▒▒░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▓▓▒▒░░▒▒▒▒▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒░░▒▒░░░░░░░░░░░░░░
██████████▓▓▓▓████████████████████████▓▓██▓▓████████████████████████████████████▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░▒▒▒▒▒▒▒▒░░░░██▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▒▒▒▒░░░░░░▒▒▒▒░░░░░░░░░░░░░░
▓▓▓▓▓▓▓▓▓▓▓▓████████████████▓▓░░░░░░░░░░░░░░░░▒▒▓▓▓▓██████████████████████▓▓████▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒░░░░████▓▓▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▓▓▒▒▓▓▒▒▒▒▒▒░░▓▓▒▒▒▒▒▒░░░░░░░░░░░░
▓▓██▓▓▓▓██████████▓▓██▓▓████░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░░░▒▒▓▓▓▓████████▓▓▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒░░▒▒░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒░░▒▒░░░░▒▒▓▓▓▓▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒░░▓▓▓▓▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░▒▒▒▒░░░░░░
▓▓██▓▓██████████████████▓▓░░░░░░░░░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▒▒▓▓██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▓▓▓▓▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒░░░░▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒▒▒░░░░▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒▓▓▒▒░░▒▒▒▒▒▒▓▓░░▒▒░░░░
▓▓██████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▓▓██▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒░░▒▒▓▓░░░░░░░░░░░░▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒▒▒▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓▒▒▒▒▓▓░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
██████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓░░░░░░▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒░░░░▓▓▒▒▒▒▓▓
██▓▓████▓▓██████▓▓████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░░░░░░░░░░░▒▒▒▒▒▒▒▒▓▓▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░▒▒▒▒░░▒▒▒▒░░░░▒▒░░░░░░▒▒▓▓▒▒▓▓▓▓░░▒▒▒▒▓▓▓▓░░▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓▒▒▒▒▒▒
██████▓▓████████████░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒░░░░░░▓▓░░▒▒░░░░▓▓▓▓▒▒▓▓▒▒▒▒░░░░▒▒▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▓▓▓▓▒▒▓▓▓▓▓▓▒▒▒▒▒▒░░▒▒░░░░▒▒░░▒▒▓▓▓▓▒▒▓▓▓▓
██▓▓██████████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒░░░░░░░░░░░░░░░░▒▒░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▓▓░░░░▒▒▒▒▒▒░░░░▒▒▒▒▒▒▓▓▒▒▓▓▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒░░░░░░░░▒▒▒▒▒▒▓▓▓▓▒▒▒▒
██████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒░░▒▒▒▒░░░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒▒▒██▓▓░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒░░░░░░░░░░▒▒▒▒░░▒▒░░▒▒▒▒░░▒▒▒▒▒▒░░░░▒▒░░░░▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒░░▒▒░░▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▒▒▒▒░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▓▓
██████▓▓████████▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒░░▒▒░░░░▒▒▒▒▒▒░░░░▒▒▓▓▒▒▓▓██▒▒▒▒░░▒▒▒▒░░▒▒░░▒▒░░▒▒░░░░▒▒▒▒▒▒▒▒░░▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒░░░░░░░░░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▓▓░░▒▒▒▒▓▓▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▓▓▒▒▓▓▒▒▒▒▓▓▒▒▓▓▒▒▒▒░░░░░░░░░░▓▓▓▓▒▒▒▒▒▒
'''

mathsTentImage = '''    '''+Green+'''
                  .e$c"*eee...                      
                z$$$$$$.  "*$$$$$$$$$.                    
            .z$$$$$$$$$$$e. "$$$$$$$$$$c.                 
         .e$$P""  $$  ""*$$$bc."$$$$$$$$$$$e.             
     .e$*""       $$         "**be$$$***$   3             
     $   =        $F              $    4$r  'F            
     $           4$F   `----      $    4$F   $       '''+Red+'''***************************'''+Green+'''     
    4P  f(x)     4$F    / \       $     $$   3r      '''+Red+'''*   Mr Becker's Tent of   *'''+Green+'''
    $"           4$F              3     $$r   $      '''+Red+'''*  Mathematical Curiosity *'''+Purple+'''      __/\__'''+Green+'''   
    $            $$F              4F    4$$   'b     '''+Red+'''***************************'''+Blue+''' . _ '''+Purple+''' \\\\''//'''+Green+'''
   dF     !      $$                b     $$L   "L         *              *       '''+Blue+'''-( )-'''+Purple+'''/_||_\\'''+Green+'''
   $             $$                $     ^$$r   "c        *              *        '''+Blue+'''.'.'''+Purple+''' \_()_/'''+Green+'''
  JF             $$            +   4r     '$$.   3L       *              *         | '''+Cyan+'''  | + \\'''+Green+'''
 .$   -     e    $$     %           $      ^$$r""         *              *         | '''+Cyan+'''  | =  \\'''+Green+'''
 $%              $$                 3r  .e*"              *              *        .'.'''+Cyan+''' ,\_____'.'''+Green+'''
'*=*********************************$$P"                \\/\/           \///                  '''+Black+'''TBE'''+END+'''
'''

outerCastleImage = '''
                                                |'''+Blue+'''>>>'''+END+'''
                                                |
                                            _  _|_  _
                                           |;|_|;|_|;|
                                           \\.    .  /
                                            \\:  .  /
                                             ||:   |
                                             ||:.  |
                                             ||:  .|
                                             ||:   |       '''+Green+'''\,/'''+END+'''
                                             ||: , |            '''+Green+'''/`\\'''+END+'''
                                             ||:   |
                                             ||: . |
              __                            _||_   |
     ____--`~    '--~~__            __ ----~    ~`---,              ___
-~--~                   ~---__ ,--~'                  ~~----_____-~'   `~----~~
'''

kettleBellImage = '''

_________________________________________________________________v_____v______
                          .-|-|------------------|-|-.           |     |
                          |         PIZZA OVEN        |_         |     |  
                     .--~~|  /\                       | -.      _|_____|_
                     |    | /__)   AND FINE ALES      |  |    ./         \.
                     |    `-.______________________.-'   |   /     YE      \\
_______________      |                                   |  /     OLDE      \\
               |     |                                   | /  KETTLE BELLE   \\
           __  |     |                                   | |  ~~~~~~~~~~~~   |
  O      ,/  | |     |                                   |  \_______________/
 <_\__--"-'  | |     |                                   |
  |\  `------' |     | _______                   _______ |
  L L          |     ||       ~---_         _---~       ||
               |     ||           ~---. .---~           ||
  PMC          |     ||               | |               ||
               |     ||               | |               ||                       _-_
_______________|     ||               | |               ||                    /~~   ~~\\
---------------'     ||            o  | |  o            ||                 /~~         ~~\\
                     ||               | |               ||   _            {               }
                     ||               | |               ||  | |            \  _-     -_  /
                     ||           .---' `---.           || /|_|\\           ~~  \\ //  ~~
                     |`.______.---'         `---.______.'||     |                | |
               ______|                                   |_\___/_                | |
--------~~~~~~~                                                  ~~~~~--------  // \\\\

'''

 

darkCaveLocation = LocationObject(0,
                                "The Dark Cave",
                                darkCaveImage,
                                ["You are in a dark and damp cave.  You see and old fire pit on the floor that has not been used for some time.",
                                "There is not much light, but you can just make out a small entrance that is blocked by a rockfall."],
                                "The rockfall looks dangerous.  You should probably not approach it!  The fire pit has ashes and various old broken items in it.",
                                [keyObject,cheeseObject,guitarStringObject],
                                [[ratObject,"A small rat emerges from a gap between the rocks and sits near the fire pit...it is looking right at you!"]],
                                10)


gloomyForestLocation = LocationObject(1,
                                "The Gloomy Forest",
                                gloomyForestImage,
                                ["You are in a dark and damp cave.  You see and old fire pit on the floor that has not been used for some time.",
                                "There is not much light, but you can just make out a small entrance that is blocked by a rockfall."],
                                "Just the sort of place that vermin might like.",
                                [pantsObject,toyBoatObject],
                                [],
                                10)

mathsTentLocation = LocationObject(2,
                                "Mr Becker's Tent of Mathematical Curiosity",
                                mathsTentImage,
                                ["You arrive at a strange looking place.  You see a dusty old tent with an even dustier looking maths teacher dressed in full ceremonial maths robes, which are far too formal for a Wednesday.",
                                "There is a strange odour in the air that is a mix of old protractors and unsolved equations. The funny looking man seems uncomfortable in the company of other humans and carries a rather retro looking slide rule.",
                                "He appears adamant that you will never solve his \"unsolveable\" mathematical riddles. He says you will never find the code and even if you did, a " + Red + "\"noob\""+ END + " couldn't use it!. Is he hiding precious treasures????"],
                                "There are many wonderful things to be seen in this place!  Mr Becker keeps muttering "+ Red + "\"quiz\"" + END + " for some reason.",
                                [anchorObject,caveTrollObject],
                                [[calcObject,"After careful searching you find an old four function calculator.  Could it be, that wielding this amazing mathematical instrument will give you special powers?  Mr Becker appears flustered by this discovery!"]],
                                30,
                                "Mr Becker says it is quite a big tent, so please be patient.")

kettleBellLocation = LocationObject(3,
                                "P Mac's Ye Olde Kettle Belle Pizzaria and Ale House",
                                kettleBellImage,
                                ["A wiff of pizza fills the air...",
                                "An outdoorsy sort of chap appears to run an old tavern selling freshly made pizzas from his own pizza oven!  A range of fine ales and spirits can also be had.",
                                "There are other strange items scattered around the room such as climbing ropes, a long skateboard and a range of tiny kettle bells that would be too light for even a small child to use."],
                                "The proprietor seems like a little odd...probably best not get too close to his tiny kettle bell collection!",
                                [brokenGuitarObject],
                                [[kettleBelleObject,"One tiny kettle bell is just within reach..."]],
                                10,
                                "Arranging tiny kettle bells and other fitness equipment.")


newWorld = [darkCaveLocation,gloomyForestLocation,mathsTentLocation,kettleBellLocation]

#Start in the cave!  room 0!!!!
currentRoom = darkCaveLocation
loadingBarNeeded = True

#SUB PROGRAMS
def ClearScreen():
    for i in range(80):
        print("")
    ##clear()
        
def PressEnterToContinue():
    input("Press enter to continue...")
    
def QuitScreen():
    #https://ascii.co.uk/text
    print(quitPageColour + '''
    
    
    
    
                                          .___                    __                        
 ___.__. ____  __ _________   _____     __| _/__  __ ____   _____/  |_ __ _________   ____  
<   |  |/  _ \|  |  \_  __ \  \__  \   / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \\ 
 \___  (  <_> )  |  /|  | \/   / __ \_/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/ 
 / ____|\____/|____/ |__|     (____  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >
 \/                                \/      \/           \/     \/                        
 
 .__                                         _____                                      
 |__| ______     _______  __ ___________   _/ ____\___________      ____   ______  _  __
 |  |/  ___/    /  _ \  \/ // __ \_  __ \  \   __\/  _ \_  __ \    /    \ /  _ \ \/ \/ /
 |  |\___ \    (  <_> )   /\  ___/|  | \/   |  | (  <_> )  | \/   |   |  (  <_> )     / 
 |__/____  >    \____/ \_/  \___  >__|      |__|  \____/|__|      |___|  /\____/ \/\_/  
         \/                     \/                                     \/               
                    
                    
    ''' + END)

def PlayAnimation():
    frames = [
        
'''
Animation test   
    ╔══════════╗
    ║ Hello    ║
    ╚══════════╝

''',
'''
Animation test   
     ╔══════════╗
     ║ Hello    ║
     ╚══════════╝

''',
'''
Animation test   
      ╔══════════╗
      ║ Hello    ║
      ╚══════════╝
''',
'''
Animation test   
       ╔══════════╗
       ║ Hello    ║
       ╚══════════╝
''',
'''
Animation test   
        ╔══════════╗
        ║ Hello    ║
        ╚══════════╝
''',
'''
Animation test   
         ╔══════════╗
         ║ Hello    ║
         ╚══════════╝
''',
'''
Animation test   
          ╔══════════╗
          ║ Hello    ║
          ╚══════════╝
'''
]

    totalFrames = len(frames)
    speed = 0.2
    
    for j in range(1,3):
      print("Loop " + str(j) + " of 5 loops.")
      for i in range(0,totalFrames):
          ClearScreen()
          print(frames[i])
          time.sleep(speed)
  
      for i in range(totalFrames-1,-1,-1):
          ClearScreen()
          print(frames[i])
          time.sleep(speed)


    
def PrintTitle():
    print(Blue + '''
   _____       .___                    __                           ________                       
  /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____    /  _____/_____    _____   ____  
 /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \  /   \  ___\__  \  /     \_/ __ \\ 
/    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/  \    \_\  \/ __ \|  Y Y  \  ___/ 
\____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >  \______  (____  /__|_|  /\___  >
        \/      \/           \/     \/                        \/          \/     \/      \/     \/
                                                            ''' + Red + ''' Version 0.2 alpha - Written by Mark Reed  ''' + END)
    
def Menu():
    print(Green + '''                 /;-._,-.____        ,-----.__
           .    (_:#::_.:::. `-._   /:, /-._, `._,
   '''+Cyan+'''+'''+Green+'''                 \   _|`"=:_::.`.);  \ __/ /
                      ,    `./  \:. `.   )==-'  .
    .      ., ,-=-.  ,\, +#./`   \:.  / /          '''+Purple+'''This game has many secrets to be found!'''+Green+'''
.           \/:/`-' , ,\ '` ` `   ): , /_  -o
       .    /:+- - + +- : :- + + -:'  /(o-) \)     .
  .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
   `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
              \:  `  X` _| _,\/'   .-'
.               ":._:`\____  /:'  /      .           .
                    \::.  :\/:'  /              '''+White+'''+'''+Green+'''
   .                 `.:.  /:'  }                '''+menuColour+'''╔══════════════════════╗'''+Green+'''
           .           ):_(:;   \   .            '''+menuColour+'''║ G - Go on thy quest  ║'''+Green+''' 
                      /:. _/ ,  |                '''+menuColour+'''║ H - High score       ║'''+Green+'''
                   . (|::.     ,`           .    '''+menuColour+'''║ A - About            ║'''+Green+'''
     .                |::.    {\                 '''+menuColour+'''║ S - Secrets          ║'''+Green+'''
                      |::.\  \ `.                '''+menuColour+'''╚══════════════════════╝'''+Green+'''
                      |:::/{ }  |     '''+Cyan+'''+'''+Green+'''             
                  ___/#\::`/ (O "==._____         ''' + END,end="")
    print("")
    print(Red + "THIS GAME IS IN THE VERY EARLY STAGES OF DEVELOPMENT.....BUT IS STILL AWESOME!!!!" + END)

def DisplayItems(theTitle,theList,needsBoxes,titleNeeded = True):
  
    if(len(theList) == 0):
        return
    
    if(titleNeeded):
      theTitle = theTitle
      UnderLine(theTitle,Black)
      
    spacesBetweenItems = 5
    columnGap = ""
    for j in range(spacesBetweenItems):
        columnGap = columnGap + " "
    
    listToDraw = []
      
    if(needsBoxes):
    
      for item in theList:
        listToDraw.append(WrapInInventoryBox(item))
      
      for i in range(0,invLines+2):
          for item in listToDraw:
              #print(item.colour,end="")
              print(item[i],end="")
              print(END,end="")
              #print(columnGap,end="")
          print("")
      print("")

    else:
      
      for i in range(0,invLines):
          for item in theList:
              print(item.colour,end="")
              print(item.imageList[i],end="")
              print(END,end="")
              print(columnGap,end="")
          print("")    
      print("")

def AreYouSure():
    while(True):
      ClearScreen()
      someAnswer = input("Are you sure you want to quit? (Y)es/(N)o")
      
      if(someAnswer.upper() == "YES" or someAnswer.upper() == "Y"):
          return True
      elif(someAnswer.upper() == "NO" or someAnswer.upper() == "N"):
          FoundSecret(secret7)
          print("Cancelling...")
          return False
      else:
          print("That is not YES or NO!!!")
          time.sleep(1.5)

def DrawPrompt():
    print(Red + "Some" + END + " of your commands are shown below: ")
    print('''
             (L)ook   (G)o               (I)nventory ''' + str(playerInventorySlots) + ''' slots   (P)ickup      (D)rop   
             (T)ouch  (A)nimation test   (S)ecrets             (H)igh score  (C)rafting table
             (Q)uit''')
    print("")
    print(Red + "Secrets" + END + " may be found by experimenting with hidden commands!")
    print("")
    someChoice = input("What will you do? ")
    someChoice = someChoice.upper()
    return someChoice
    
def DisplaySecrets():
    #https://patorjk.com/software/taag/#p=display&f=Graffiti&t=of%20secrets
    ClearScreen()
    print(Blue + '''
    
 ___________.__             __________                       
 \__    ___/|  |__   ____   \______   \ ____   ____   _____  
   |    |   |  |  \_/ __ \   |       _//  _ \ /  _ \ /     \\ 
   |    |   |   Y  \  ___/   |    |   (  <_> |  <_> )  Y Y  \\
   |____|   |___|  /\___  >  |____|_  /\____/ \____/|__|_|  /
                 \/     \/          \/                    \/ 
        _____                                      __          
  _____/ ____\   ______ ____   ___________   _____/  |_  ______
 /  _ \   __\   /  ___// __ \_/ ___\_  __ \_/ __ \   __\/  ___/
(  <_> )  |     \___ \\  ___/\  \___|  | \/\  ___/|  |  \___ \\ 
 \____/|__|    /____  >\___  >\___  >__|    \___  >__| /____  >
                    \/     \/     \/            \/          \/ 
  
    '''+END)
    
    PrintSecretsFoundFullData()
    PressEnterToContinue()

def PrintSecretsFoundData():
  #count the secrets that we have found
  numFound = 0
  totalNumOfSecrets = len(secretsList)
  for someSecret in secretsList:
    if(someSecret.achieved):
      numFound = numFound + 1
  
  if(numFound != totalNumOfSecrets):
    print(Red + str(numFound) + " of " + str(totalNumOfSecrets) + " secrets found!" + END)
  else:
    print(Green + str(numFound) + " of " + str(totalNumOfSecrets) + " secrets found!" + END)
    
  print("")
    
def PrintSecretsFoundFullData():
  
  #secrets found will be green
  #print unfound secrets in red
  
  numFound = 0
  totalNumOfSecrets = len(secretsList)
  num = 1
  for someSecret in secretsList:
    numToPrint = str(num)
    if(len(numToPrint) == 1):
      numToPrint = numToPrint + " "
    print(numToPrint + " : ",end="")
    num = num + 1
    
    colWidth = 55
    theClue = someSecret.clue
    
    spacesToAdd = colWidth - len(theClue)
    
    for i in range(spacesToAdd):
      theClue = theClue + " "
    
    print(theClue, end="")
    
    if(someSecret.achieved):
      numFound = numFound + 1
      print(Green + someSecret.achievedString  + END)
    else:
      print(Red + "LOCKED"  + END)
  
  PrintChaliceStatus()
  PrintMrBeckerStatus()
  PrintPMacStatus()
  PrintCombosMade()
  
  print("")  
  
  if(numFound != totalNumOfSecrets):
    print(Red + str(numFound) + " of " + str(totalNumOfSecrets) + " secrets found!" + END)
    print("")
    print(Red + "Your quest is not over...there are secrets to be found!" + END)
  else:
    print(Green + str(numFound) + " of " + str(totalNumOfSecrets) + " secrets found!" + END)
    print("")
    print(Green + "You are quite the gamer...you found all secrets.  Well done!" + END)
  print("")


def PrintPMacStatus():
 print("P Mac\'s kettle bell rating  : " + Red + "Noob" + END)

def PrintMrBeckerStatus():
  if(mrBeckerQuizDone):
    print("Mr Becker\'s opinion of you  : " + Green + "No longer a noob" + END)
  else:
    print("Mr Becker\'s opinion of you  : " + Red + "Noob" + END)

def PrintCombosMade():
  print("Combos crafted              : " + Blue + str(combosMade) + END)
  
def PrintChaliceStatus():
  status = GetChaliceStatus()
  print("")
  
  print(Black + "\"Chalice of Destiny\" status : " + status)

def GetChaliceStatus():
  if(chaliceFound == False):
    return Blink + Red + "Lost and certainly NOT safe!" + END
  elif(chaliceFound == True and chaliceSafe == False):
    return Green + "Located," + Blink + Red + " but it is not yet safe!" + END
  elif(chaliceFound == True and chaliceSafe == True):
    return Green + "Located and safe...impressive!" + END
  


def AboutTheDeveloper():
  #https://www.text-image.com/convert/pic2ascii.cgi
  print('''
::////////////////////+oosssssyhdyo+++++++++++++++
::::://////////////oooyhhhhddhdmdhysoo++++++++++++
:::::::::////////+shhyhdddddhyyyhhdddddhys++++++++
::::::::::://///+shdmdmmmNNmmmmmddddmmmmdho+++++++
:::::::::::::/+syydddddddmmNNNMMMMNNNmmmmdo+////++
:::::::::///+ohhhys++/////++oshdmNNMNNNmddyo+/////
::::::::://osyyo:------:::/:///++sydmNNNdhyo//////
------::/+syys:------:::://++//+++osyhmNNmys+/////
......-osyys+:------:::////++++++ooossyhmmmhs/:::/
``````:yyyo/::::::::://////++++++oossssyyhdmds::::
......:yyo/:::/::::://++ooooooooosyyyyyssyhhds::::
------/syo/::///:://+oossyssysosssyyyyyyysyhhs::::
------:os+://+ossyyhhyyyyyyyhyyhhhhhhhhhyssyhy+:::
:::--:/sy+//ossyhhdddddhhhhhhddddddhhhyyyysyhho---
:::--:+ss+/+syyyyhdddddddyyhhmddddddhhhyyysydho---
::::::osso+oyyyshmmmdmddy/+shmdmdmmmhhhhyysyhh/---
:::::-/oso++++/+oyhdddhs:-:+ydddddddhyyyyysyho----
:::::-:/so////+osyhhhy+/:-:+yhhdddhhhhyyyysyy:----
::::----/++++//+oooo++//:-:oshhhhhhhhyyyyysso-----
:::---...:+++//+//+osyo:::/oshdhhhyyyyyyyyso------
::::---..:++///+ossyhh+++osyyyhdhhyyyyyyyys+------
::::-----/+++osyyhhhhyohhhhhhdddhhhyyyyyyyyo------
::::::---/+oyyhhhdhhyo+oydddddddhhhhhyyyyyso------
/::::::--:+syddyyhhhhyooyddddhhhhhhhhyhhyys/------
//:::::---/oydyoyhdmmhsyhddddhhdddhhhyhhyso-------
////:::::::oyhsshddhysosyhhhhhyyhhhhhyhyyo--------
///////:::::oyyyddyssosyhhhhhhyyyyhhhyhyo---------
////////:::-/oyhyysooooosyyhhyyyyyhhhyys-.--------
/////::---..:ooyyysso++++oossyyyyyyyyys+:---------
/::-.``.-.`.-+ooyhysoooosyyyyyyyhyyyyso/++++///::-
//-```.-.`-/./oosyyyyyyyyhhyhyyhyyyyss+/o//o+:/+//
/.```.-.`/h/.-+oosyyyyyyyyyyyyyyyyysso/so/:++:-://
-.```....dm/-.-+ossyyyyyyyyyyyyyyysss/:ho:++/---+/
..`...::+mmo----/osyyyyyyyyyyyyyyyyo/:oNy++/:---/+
-.....-/omds------/syyyyyyyyyyyys+/:::dNh+o/:---//''')
  print(Blue + "   An adventure game brought to you by Mr Reed!" + END)
  FoundSecret(secret4)
    
def FoundSecret(theSecret,continueMessage = True):
    if(theSecret.achieved == False):
      # the player has found a secret!!!
      theSecret.achieved = True
      print("")
      print(theSecret.foundString)
      PrintSecretsFoundData()
      print("")
    if(continueMessage):
      PressEnterToContinue()

def TouchAtLocation():
  print("This game feature is not yet working.")
  PressEnterToContinue()

def DrawProgressBar(segments,someTime,theMessage):
  print(theMessage)
  
  if(testing):
    return
  
  print("")
  for i in range(segments):
    print("▓",end="")
    time.sleep(someTime)
  print("   done!")
  print("")
  
def RemoveObjectFromGameList(someList,objectToRemove):
  #remove the object passed in from the given list (usually the inventory) and replace with the nothing object
  
  for x in range(0,len(someList)):
      if (someList[x].name.upper() == objectToRemove.name.upper() ):
          someList[x] = nothingObject
          return

def IsItInTheList(someList,someItemName):
  for thing in someList:
    if thing.name.upper() == someItemName.upper():
      #input("Found it")
      return thing
  #input("Not there!!!")
  return None
  
def DrawCurrentRoom():
  
    global currentRoom
    global mrBeckerQuizDone
    global timesQuizSaid
    global loadingBarNeeded
    
    while(True):
        global chaliceFound
      
        #Based on the currentRoom variable we can be in various places!
        
        roomNum = currentRoom.num
        roomTitle = currentRoom.name
        roomDescription = currentRoom.description
        roomItems = currentRoom.locationItems
        roomLookText = currentRoom.extraDescription
        roomLookItems = currentRoom.extraItems
        roomPhoto = currentRoom.image
        roomLoadingMessage = currentRoom.locationLoadingMessage
        roomLoadingTime = currentRoom.loadingTime
        
        if(loadingBarNeeded):
          ClearScreen()
          print(roomPhoto)
          theMessage = "Loading adventure items for " + Blue + roomTitle + END + "..." + roomLoadingMessage
          DrawProgressBar(roomLoadingTime,0.2,theMessage)
          loadingBarNeeded = False
          input("Press enter to do adventuring at this location...")
          
        if(currentRoom.beenBefore == False):
          currentRoom.beenBefore = True
        ClearScreen()
        print(roomPhoto)
        UnderLine(roomTitle,roomTitleColour)
        
        for line in roomDescription:
          print(line)
        print("")
        
        DisplayItems("Items in " + roomTitle,roomItems,False)
        
        playerAction = DrawPrompt()
        if(playerAction=="I"):
            ClearScreen()
            DisplayItems("your inventory",inventory,True)
            PressEnterToContinue()
        elif(playerAction in NiceThingsAboutMe):
          FoundSecret(secret1)
        elif(currentRoom == mathsTentLocation and  playerAction == "HELLO MR BECKER"):
          FoundSecret(secret12)
        elif(currentRoom == mathsTentLocation and playerAction == "QUIZ"):
          timesQuizSaid = timesQuizSaid + 1
          
          if(timesQuizSaid == 5):
            DrawProgressBar(40,0.2,"Oooh a secret quiz.  Mr Becker says it is a really good one, so this will take some time to load....")            
            timesQuizSaid = 0
            won = StartBeckerQuiz()
            if(won == False):
              currentRoom = darkCaveLocation
              print("\"You do not deserve to be in the company of a man such as me!..." + Red + "noob!\"" + END)
              print("")
              print("After his rant, he casts you immediately back to the cave!  You were finding him quite odd, so are glad to be on your way.")
              loadingBarNeeded = True
              PressEnterToContinue()
              continue
              
          elif(timesQuizSaid == 1):
            print("Nothing happens...but Mr Becker glances briefly in your direction?!?")
            PressEnterToContinue()
          elif(timesQuizSaid == 2):
            print("Nothing happens...but Mr Becker drops his slide rule and stares at you like a crazy man!")
            PressEnterToContinue()
          elif(timesQuizSaid == 3):
            print("Nothing happens...but Mr Becker begins to weep uncontrollably.  You pity this strange man.")
            PressEnterToContinue()
          elif(timesQuizSaid == 4):
            print("Nothing happens...but Mr Becker sheepsihly glances from side to side in a cowardly manner.  You pity him more that you did a moment ago.")
            PressEnterToContinue()
          else:
            print("Nothing happens...keep going perhaps?")
            PressEnterToContinue()
           
          
          
        elif(currentRoom == mathsTentLocation and playerAction == str(randomCode) and calcObject not in inventory and chaliceFound == False):
          print("The calculator fizzes with a magical glow and all of a sudden...",end="")
          time.sleep(1.5)
          print("3...",end="")
          time.sleep(1)
          print("2...",end="")
          time.sleep(1)
          print("1...",end="")
          time.sleep(1)
          print("nothing happens!")
          time.sleep(1)
          print("Mr Becker has a smug look on his face and holds his slide rule aloft in an attempt at a triumphant pose.  You begin to pity the poor man.")
          PressEnterToContinue()
        elif(currentRoom == mathsTentLocation and playerAction == str(randomCode) and calcObject in inventory and chaliceFound == False and mrBeckerQuizDone == False):
          print("The calculator makes a strange popping sound and a magical glow appears around the device, and then...",end="")
          time.sleep(1.5)
          print("3...",end="")
          time.sleep(1)
          print("2...",end="")
          time.sleep(1)
          print("1...",end="")
          time.sleep(1)
          print("you panic, as nothing at all happens.  How embarrassing.")
          print("")
          print("Mr Becker laughs at you and chants " + Red + "\"NOOB NOOB NOOB\"" + END +" then goes back to muttering "+ Red + " \"quiz\"" + END + ". You pity and admire him in equal measure.")
          PressEnterToContinue()
        elif(currentRoom == mathsTentLocation and playerAction == str(randomCode) and calcObject in inventory and chaliceFound == False and mrBeckerQuizDone == True):
          print("No longer a noob, you are now skilled enough to wield the calculator and...",end="")
          time.sleep(3)
          print("you notice it has a nice solar panel in the event of battery failure, but that may not be relevant.")
          time.sleep(3)
          print("The wonderful machine begins to emit the most magical of sounds and smoke pours from the device.")
          time.sleep(3)
          print("Mr Becker looks quite sad now.")
          time.sleep(2)
          print("A most wonderful and enchanting object transmogrifies before your very eyes!!! Once feared lost in time, the \"Chalice of Destiny\" sits magestically before you!!!")
          time.sleep(3)
          print("")
          print("The calcualtor is gone forever and Mr Becker begins to cry.  You are worried for his safety as he clearly isn\'t looking after himself.")
          chaliceFound = True
          FoundSecret(secret13,False)
          PressEnterToContinue()
          currentRoom.locationItems.append(chaliceObject)
          
          for x in range(0,len(inventory)):
            if (inventory[x].name == "calculator" ):
              inventory[x] = nothingObject
    
        elif(playerAction == "A"):
          PlayAnimation()
        elif(playerAction == "S"):
          DisplaySecrets()
        elif(playerAction == "T"):
          TouchAtLocation()
        elif(playerAction == "G"):
            ClearScreen()
            someString = "Places in the world:"
            UnderLine(someString,Black)
            
            thePlaceNumbers = []
            
            for location in newWorld:
              print(str(location.num)+ " : " + location.name)
              thePlaceNumbers.append(location.num)
            print("")
            
            newPlace = input("Where will you go?")
            
            if(newPlace.upper() == "HOME"):
              FoundSecret(secret3)
              continue
            
            if(newPlace.isdigit()):
              newPlace = int(newPlace)
              if(currentRoom.num == newPlace):
                print("Staying where we already are...cowardly at best.")
                FoundSecret(secret8,False)
                PressEnterToContinue()
                loadingBarNeeded = False
                  
              else:
                if(newPlace in thePlaceNumbers):
                  
                  #find the location with this number
                  for location in newWorld:
                    if(location.num == newPlace):
                        currentRoom = location
                        #print("Moving to " + currentRoom.name + "...")
                        loadingBarNeeded = True
                        #PressEnterToContinue()  
                        break
                        
                else:
                  print("That is a not a place I can go!")
                  PressEnterToContinue()
            
            else:
              print("That is a not a place I can go!")
              PressEnterToContinue()
      
        elif(playerAction == "L"):
            if(roomLookText != ""):
                print("")
                print("You carefully study this place...")
                print("")
                print(roomLookText, end = " ")
                
                #Also add items that can now been seen following the look
                for item in roomLookItems:
                  print(item[1], end = " ")
                  roomItems.append(item[0])
                  roomLookItems.remove(item)
                print("")
            else:
                print("There is nothing else to see.")
            PressEnterToContinue()
        elif(playerAction == "H"):
            DoHighScore()
        elif(playerAction == "Q"):
            answer = AreYouSure()
            if(answer == True):
              ClearScreen()
              QuitScreen()
              PressEnterToContinue()
              break
            else:
              continue
              
        elif(playerAction=="P"):
          
            numberOfThingsInInvetory = 0
            for item in inventory:
              if item.name != "nothing":
                numberOfThingsInInvetory = numberOfThingsInInvetory + 1
              
          
          
            if(numberOfThingsInInvetory >= playerInventorySlots):
                print("You are carrying your maximum of " + str(playerInventorySlots) + " things already!")
                PressEnterToContinue()
                
            elif(len(roomItems) > 0):
                while(True):
                    
                    thingsInRoom = []
                    for thing in roomItems:
                        thingsInRoom.append(thing.name.upper())
                    ClearScreen()
                    
                    DisplayItems("Items in "+ roomTitle,roomItems,False)
                    
                    print("If you have changed your mind about picking up an item you may (C)ancel.")
                    thingToPickup = input("What do you want to pick up?")
                    
                    if(thingToPickup.upper() != "C"):
                        if(thingToPickup.upper() in thingsInRoom):
                          
                            if(thingToPickup.upper() == "CALCULATOR"):
                              print("There is note on the back of the calculator from Mr Becker. It states that it is too powerful for a " + Red +"\"noob\""+END+" to safely wield.")
                          
                            print(thingToPickup + " now in inventory.")
                            
                            #remove it from the room item list
                            pos = 0
                            for thing in roomItems:
                                if(thingToPickup.upper() != thing.name.upper()):
                                    pos = pos + 1
                                else:
                                    #found it
                                    
                                    #find pos of first nothingObject
                                    for x in range(0,len(inventory)):
                                      if(inventory[x].name == "nothing"):
                                        inventory[x] = thing
                                        break
                                    
                                    roomItems.pop(pos)
                                    break
                                      
                            #add it to our inventory
                            
                            PressEnterToContinue()
                            break
                        else:
                            print(thingToPickup + " is not an item that can be picked up right now!")
                            PressEnterToContinue()
                    else:
                        print("Cancelling...")
                        PressEnterToContinue()
                        break
            else:
                print("There is nothing to pick up!")
                PressEnterToContinue()
                
        elif(playerAction == "C"):
          GetCrafty()
        elif(playerAction == "D"):
          
            numberOfThingsInInvetory = 0
            for item in inventory:
              if(item.name != "nothing"):
                numberOfThingsInInvetory = numberOfThingsInInvetory + 1
          
            if(numberOfThingsInInvetory > 0):
                while(True):
                    
                    thingsInYourInventory = []
                    for thing in inventory:
                      if(thing.name != "nothing"):
                        thingsInYourInventory.append(thing.name.upper())
                    ClearScreen()
                    
                    DisplayItems("Things that can be dropped",inventory,True)
                    
                    print("If you have changed your mind about dropping an item you may (C)ancel.")
                    thingToDrop = input("What do you want to drop?")
                    
                    #C would mean cancel!!!
                    if(thingToDrop.upper() != "C"):
                        if(thingToDrop.upper() == "TROUSERS" or thingToDrop.upper() == "MY TROUSERS"):
                            FoundSecret(secret2)
                            break
                            
                        #is it something we are carrying?
                        theObjectToDrop = IsItInTheList(inventory,thingToDrop.upper())
                        
                        #input(theObjectToDrop.name)
                        
                        if(theObjectToDrop != None):
                            print(theObjectToDrop.name + " dropped.")
                            
                            #remove it from the inventory item list
                            RemoveObjectFromGameList(inventory,theObjectToDrop)
                            
                            #not all objects end up in the room...some secrets just drop from inv and are gone!
                            if(theObjectToDrop == fatRatObject and currentRoom == gloomyForestLocation):
                                FoundSecret(secret11,False)
                                #don't put the fat rat down in this room...it is gone forever now!
                                PressEnterToContinue()
                                break
                              
                            elif(theObjectToDrop == ratObject and currentRoom == gloomyForestLocation):
                                print("It would be better if I " + Red + "fed"+ END+" the poor thing before I released it!")
                                #this will end up in the room item list due to the append after this if statement :)
                            elif(theObjectToDrop == caveTrollObject and currentRoom == darkCaveLocation):
                                FoundSecret(secret19,False)
                                #don't put the troll down in this room...it is gone forever now!
                                PressEnterToContinue()
                                break
                                    
                            #all other things can just be dropped into room item list
                            roomItems.append(theObjectToDrop)
                            PressEnterToContinue()
                            break
      
                        else:
                            print(thingToDrop + " is not an item that can be dropped right now!")
                            PressEnterToContinue()
                    else:
                        print("Cancelling...")
                        PressEnterToContinue()
                        break
            else:
                print("You are not carrying anything.")
                PressEnterToContinue()
        else:
            print("I cannot do that!")
            PressEnterToContinue()

def GetCrafty():
  global combosMade
  numOfNonEmpty = 0
    
  for x in range(0,len(inventory)):
    if(inventory[x].name != "nothing"):
      numOfNonEmpty = numOfNonEmpty + 1
  
  #display the three crafting table sections...then will be blank at first!
  craftingItemList = [nothingObject,nothingObject,nothingObject]
    
  while(True):
    #we can only craft with 2 or more items in our inventory
      
    if(numOfNonEmpty < 2):
      print("You cannot craft combos without at least 2 items in your inventory!")
      PressEnterToContinue()
      return
    
    ClearScreen()
    
    DisplayItems("",inventory,True,False)
    
    print('''  
   __                                    __
   ||    What items from your inventory  ||
   ||          would you like            ||
  ----       to craft togehter?         ----
  \  /                                  \  /
   \/                                    \/             ''')
    
    DisplayItems("",craftingItemList,True, False)
    print("Type the item name to add it to the crafting table  or (R)estart (C)ombo (Q)uit.")
    theChoice = input("Choice : ")
    theChoice = theChoice.upper()
    
    if(theChoice == "Q"):
      return
    elif(theChoice == "R"):
      craftingItemList = [nothingObject,nothingObject,nothingObject]
    elif(theChoice == "C"):
    
      #is it a combo?
    
      for someCombo in comboList:
        thingsNeeded = []
        numFound = 0
        numRequired = len(someCombo.comboItemList)
        
        numOfNonNothingsInCraftingList=0
        for thingy in craftingItemList:
          if(thingy.name != "nothing"):
            numOfNonNothingsInCraftingList = numOfNonNothingsInCraftingList + 1
            
        if(numRequired != numOfNonNothingsInCraftingList):
          #wrong number of items, so can't be right!
          break
        
        for craftItem in craftingItemList:
          if(craftItem in someCombo.comboItemList):
            numFound = numFound + 1
            thingsNeeded.append(craftItem)
            
            if(numFound == numRequired):
              #got one!
              print(someCombo.successMessage)
              combosMade = combosMade + 1
              FoundSecret(secret18,False)
              PressEnterToContinue()
              
              #remove all of thingsneeded from inventory
              for thingNeeded in thingsNeeded:
                for z in range(0,len(inventory)):
                  if(inventory[z].name.upper() == thingNeeded.name.upper()):
                    inventory[z] = nothingObject
              
              #add new item(s) to current inventory...there will always be at least 2 spaces due to what we just lost above
              for newItem in someCombo.resultItemList:
                for z in range(0,len(inventory)):
                  if inventory[z].name == "nothing":
                    inventory[z]= newItem
                    break
              
              return
                  
    else:
      #look to see if they type a proper item name
      
      bFoundIt = False
      bAlreadyIn = False
          
      for item in inventory:
        if(item.name.upper() == theChoice):
          
          #cant add it twice
          for thisAlreadyInList in craftingItemList:
            if(thisAlreadyInList.name.upper()== theChoice):
              bAlreadyIn = True
          
          if(bAlreadyIn):
            break
          
          #it is a valid item!
          #add it to first nothingObject slot
          for x in range(0,len(craftingItemList)):
            if(craftingItemList[x].name == "nothing"):
              craftingItemList[x] = item
              bFoundIt = True
              break
            
      #if we get this far the item was not valid
      if(bFoundIt == False and bAlreadyIn == False):
        input("No such item.  Press enter to try again")
          
      
  PressEnterToContinue()
  

def StartBeckerQuiz():
  
  FoundSecret(secret14)
  #return True if they win
  global mrBeckerQuizDone
  global timesQuizSaid
  numOfQuestions = 5
  ClearScreen()
  print(Blue+'''
__________               __               /\         ________        .__        
\______   \ ____   ____ |  | __ __________)/ ______  \_____  \  __ __|__|_______
 |    |  _// __ \_/ ___\|  |/ // __ \_  __ \/  ___/   /  / \  \|  |  \  \___   /
 |    |   \  ___/\  \___|    <\  ___/|  | \/\___ \   /   \_/.  \  |  /  |/    / 
 |______  /\___  >\___  >__|_ \\___  >__|  /____  >  \_____\ \_/____/|__/_____ \\
        \/     \/     \/     \/    \/           \/          \__>              \/
  ''')
  print(Red + "                           ADVANCED MATHS CHALLENGE FOR EXPERTS ONLY" + END)
  print("")
  
  print(Purple + '''
              _________________________________________________
           - /                                                 \\
          /  | You will never answer my impossible questions!! |
     __/\__  \_________________________________________________/
. _  \\\\''// 
-( )-/_||_\\
 .'. \_()_/
  |   | + \\
  |   | =  \\
 .'. ,\_____'.
           '''+Black+'''TBE
  
  '''+END)
  
  score = 0
  for i in range(1,numOfQuestions+1):
    num1 = random.randint(1,12)
    num2 = random.randint(1,12)
    theAnswer = num1*num2
    while(True):
      print("Question " + str(i) + " of " + str(numOfQuestions))
      userAnswer=input(str(num1) + " X " + str(num2) + " = ")
      if(userAnswer.isdigit()):
        userAnswer = int(userAnswer)
        break
      else:
        print("Numbers only!")
      
    if(userAnswer == theAnswer):
      score = score + 1
      print("Correct")
    else:
      print("Fail!")
  
  if(score == numOfQuestions):
  
    FoundSecret(secret16)
    print("Mr Becker congratulates you on your super maths skills.  He mutters something about you " + Green + "no longer being a noob!" + END)
    print("He suggests you use your new found powers wisely.  You are glad the quiz is over and worry about how he copes on his own.")
    mrBeckerQuizDone = True
    PressEnterToContinue()
    return True

  else:
    mrBeckerQuizDone = False
    print("Mr Becker says that your maths skills are not at the level required to impress a man of his intelligence!")
    FoundSecret(secret17,False)
    return False
    
  
def UnderLine(theWord,theColour):
    print(theColour + theWord)
    for letter in theWord:
        print("═",end="")
    print("" + END)

#def CheckName(someName):
#  theName = someName.upper()
#  theName = theName.replace(" ", "")
#  for badword in someWords:
#    if(UnencryptWord(badword,-1) in theName):
#      return False
#  return True

def MyInput(someString):
  print(someString,end="")
  theInput = sys.stdin.readline().rstrip()
  return theInput
    
def RunGame():
  global playerName
  global startType
  global startLevel
  
  #return players can change name if they want...
  while(True):
      ClearScreen()
      
      print(Blue + '''
__________              .__                      __  .__          __  .__    .__               
\______   \ ____   ____ |__| ____   ____   _____/  |_|  |__     _/  |_|  |__ |__| ____   ____  
 |    |  _// __ \ / ___\|  |/    \ /    \_/ __ \   __\  |  \    \   __\  |  \|  |/    \_/ __ \\ 
 |    |   \  ___// /_/  >  |   |  \   |  \  ___/|  | |   Y  \    |  | |   Y  \  |   |  \  ___/ 
 |______  /\___  >___  /|__|___|  /___|  /\___  >__| |___|  /    |__| |___|  /__|___|  /\___  >
        \/     \/_____/         \/     \/     \/          \/               \/        \/     \/ 
                                                 __          __  .__     
                    ________ __   ____   _______/  |_  _____/  |_|  |__  
                   / ____/  |  \_/ __ \ /  ___/\   __\/ __ \   __\  |  \\ 
                  < <_|  |  |  /\  ___/ \___ \  |  | \  ___/|  | |   Y  \\
                   \__   |____/  \___  >____  > |__|  \___  >__| |___|  /
                      |__|           \/     \/            \/          \/    
      
      ''' + END)
  
      if(playerName != "None"):
          FoundSecret(secret10,False)
          print("You may want to change your name.  Previously you were called " + playerName + ".")
  
      startType = "Trainee wizard"
      startLevel = "I"
      playerName = MyInput("Welcome brave adventurer, what is thy name? ")
      if(playerName == ""):
        print("Stories cannot be written of your bravery if you remain nameless!")
        FoundSecret(secret9)
      elif(playerName.upper() == "MR REED"):
        
        FoundSecret(secret15,False)
        print("Name not allowed.")
        PressEnterToContinue()
      #elif(CheckName(playerName)==False):
      #  print("You cannot have that name!")
      #  PressEnterToContinue()
      else:
        break

  
  print("")
  print("Welcome " + Blue + playerName + END + ". You are a " + Blue + startType + END + " level " + Blue + startLevel + END + ".")
  print("")
  print("Inventory slots                : " + Blue + str(playerInventorySlots) + END)
  print("\"Chalice of Destiny\" status    : " + GetChaliceStatus())
  print("Current item combo score       : " + Blue + str(combosMade) + END)
  print("Enchantment coefficient        : " + Blue + "0" + END)
  print("Most used magic item           : " + Blue + "none...yet!" + END)
  print("")
  print(Green + '''          ,    _
         /|   | |
       _/_\_  >_<
      .-\-/.   |      <---  MASSIVE NOOB
     /  | | \_ |
     \ \| |\__(/
     /(`---')  |
    / /     \  |
 _.'  \'-'   /  |
 `----'`=-='   ' 
  ''' + END)
  input("Press enter to go on thyeth questeth...")
  DrawCurrentRoom()

def SavePlayerNameToFile(newName):
  timeNow = str(datetime.datetime.now())
  with open("SavedGames.txt","a") as the_file:
    the_file.write(newName + "," + timeNow + '\n')  
    the_file.close()
    
def DoHighScore():
        ClearScreen()
        
        print(Blue + '''  ___ ___ .__       .__         _________                           
 /   |   \|__| ____ |  |__     /   _____/ ____  ___________   ____  
/    ~    \  |/ ___\|  |  \    \_____  \_/ ___\/  _ \_  __ \_/ __ \ 
\    Y    /  / /_/  >   Y  \   /        \  \__(  <_> )  | \/\  ___/ 
 \___|_  /|__\___  /|___|  /  /_______  /\___  >____/|__|    \___  >
       \/   /_____/      \/           \/     \/                  \/ 
        ''' + END)
        
        print(Purple + '''              _,-'|
           ,-'._  |
 .||,      |'''+Black+'''####'''+Purple+'''\ |             
'''+Red+'''\.`',/'''+Purple+'''     \\'''+Black+'''####'''+Purple+'''| |             '''+Black+'''Name of adventurer        : ''' + Green + '''Mr Reed''' + Purple + '''
'''+Red+'''= ,. ='''+Purple+'''      |'''+Black+'''###'''+Purple+'''| |             '''+Black+'''High score                : ''' + Green + '''12970 points''' + Purple + '''
'''+Red+'''/ || \\'''+Purple+'''    ,-'\\'''+Black+'''#'''+Purple+'''/,'`.            '''+Black+'''Player XP                 : ''' + Green + '''30545 XP''' + Purple + '''
  ||     ,'   `,,. `.           '''+Black+'''Character upgrade level   : ''' + Green + '''Alchemist level IV''' + Purple + '''
  ,|____,' , ,;' \| |           '''+Black+'''Secrets found             : ''' + Green + '''All secrets found!!!''' + Purple + '''
 (3|\    _/|/'   _| |           '''+Black+'''\"Chalice of Destiny\"      : ''' + Green + '''Located and returned to its rightful place''' + Purple + '''
  ||/,-''  | >-'' _,\\\\          '''+Black+'''Item combo score          : ''' + Green + '''100% + all bonus combos''' + Purple + '''
  ||'      ==\ ,-'  ,'          '''+Black+'''Enchantment coefficient   : ''' + Green + '''x16 + invisibility cloak''' + Purple + '''
  ||       |  V \ ,|            '''+Black+'''Most used magic item      : ''' + Green + '''The mirror of disgruntlement''' + Purple + '''
  ||       |    |` |
  ||       | M |   \\      ''' + Blue + '''A true master of the game...an unbeatable score from a gaming legend!''' + Purple + '''
  ||       | P  \    \\
  ||       | R   |    \\
  ||       |      \_,-'
  ||       |___,,--")_\\
  ||         |_|   ccc/
  ||        ccc/
        '''+END)
        
        FoundSecret(secret6)

#def ReadWordsFromFile(file_name):
#  with open(file_name) as file:
#      for line in file:
#          someWords.append(line.rstrip())
#      file.close()
 
def LoadSavedGames():
  print("Attempting to look for saved games...this feature does not work yet!")
  with open("SavedGames.txt") as file:
      for line in file:
          print(line)
      file.close() 
  input("Press enter to continue...")

def UnencryptWord(word,shift):
  newWord = ""
  for letter in word:
    newLetter = chr(ord(letter)+shift)
    newWord = newWord + newLetter
  return newWord
  
#MAIN BODY
menuSpammed = 0  # part of a secret!
randomnum = random.randint(20000000,80000000)
DrawProgressBar(8,0.3,"Please wait for the game realm to be constructed using random world seed : " + str(randomnum))
         
#ReadWordsFromFile("NamesNotAllowed.txt")
#LoadSavedGames()

while(True):
    ClearScreen()
    PrintTitle()
    Menu()
    print(Red + "Secrets" + END + " may be found by experimenting with hidden commands!")
    print("")
    
    theChoice = input("Please select an option: ")
    
    if(theChoice.upper() == "H"):
        DoHighScore()
    elif(theChoice.upper() == "G"):
        ClearScreen()
        RunGame()
    elif(theChoice.upper() == "S"):
        DisplaySecrets()
    elif(theChoice.upper() == "A"):
        ClearScreen()
        AboutTheDeveloper()
    elif(theChoice.upper() in NiceThingsAboutMe):
        FoundSecret(secret1)
    else:
      if(secret5.achieved == False):
        menuSpammed = menuSpammed + 1
        if(menuSpammed == 20):
          print("Why are you doing this?")
          PressEnterToContinue()
        elif(menuSpammed == 40):
          print("Keep going!")
          PressEnterToContinue()
        elif(menuSpammed == 70):
          print("Persistence pays in the end...")
          PressEnterToContinue()
        elif(menuSpammed == 100):
          FoundSecret(secret5)
        
