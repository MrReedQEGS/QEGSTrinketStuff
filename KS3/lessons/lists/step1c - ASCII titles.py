#################################################
# HOW TO PRINT AN ASCII ART TITLE ABOVE A LIST
#
# Written by Mr Reed
#################################################

##########################
# Variables
##########################
myTopLeft = "╔"
myTopRight = "╗"
myBotLeft = "╚"
myBotRight = "╝"
myHorizontal = "═"
myVertical = "║"
myDividerLeft = "╠"
myDividerRight = "╣"

dogs = ["poodle","labrador","spaniel","setter"]

##########################
# Main program
##########################

print("""
╔═══════════╗
║ Some dogs ║
╚═══════════╝
""")

for currentItem in dogs:
  print( currentItem)

  
  
  
  
  
