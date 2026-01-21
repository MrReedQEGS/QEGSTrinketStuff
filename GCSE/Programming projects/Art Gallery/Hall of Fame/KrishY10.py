#STUDENT NAME : Krish Daru
#Paste your final art gallery code in here...

#Importing random module so that randomised colours can be used later on
import random

#Importing time module so that animations can be used
import time

END ="\033[0m" # End formatting

Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White
DarkCyan = '\033[36m'     # Dark cyan

# Bold
BBlack="\033[1;30m"       # Black
BRed="\033[1;31m"         # Red
BGreen="\033[1;32m"       # Green
BYellow="\033[1;33m"      # Yellow
BBlue="\033[1;34m"        # Blue
BPurple="\033[1;35m"      # Purple
BCyan="\033[1;36m"        # Cyan
BWhite="\033[1;37m"       # White

# Underline
UBlack="\033[4;30m"       # Black
URed="\033[4;31m"         # Red
UGreen="\033[4;32m"       # Green
UYellow="\033[4;33m"      # Yellow
UBlue="\033[4;34m"        # Blue
UPurple="\033[4;35m"      # Purple
UCyan="\033[4;36m"        # Cyan
UWhite="\033[4;37m"       # White

# Background
On_Black="\033[40m"       # Black
On_Red="\033[41m"         # Red
On_Green="\033[42m"       # Green
On_Yellow="\033[43m"      # Yellow
On_Blue="\033[44m"        # Blue
On_Purple="\033[45m"      # Purple
On_Cyan="\033[46m"        # Cyan
On_White="\033[47m"       # White

# High Intensty
IBlack="\033[0;90m"       # Black
IRed="\033[0;91m"         # Red
IGreen="\033[0;92m"       # Green
IYellow="\033[0;93m"      # Yellow
IBlue="\033[0;94m"        # Blue
IPurple="\033[0;95m"      # Purple
ICyan="\033[0;96m"        # Cyan
IWhite="\033[0;97m"       # White

# Bold High Intensty
BIBlack="\033[1;90m"      # Black
BIRed="\033[1;91m"        # Red
BIGreen="\033[1;92m"      # Green
BIYellow="\033[1;93m"     # Yellow
BIBlue="\033[1;94m"       # Blue
BIPurple="\033[1;95m"     # Purple
BICyan="\033[1;96m"       # Cyan
BIWhite="\033[1;97m"      # White

# High Intensty backgrounds
On_IBlack="\033[0;100m"   # Black
On_IRed="\033[0;101m"     # Red
On_IGreen="\033[0;102m"   # Green
On_IYellow="\033[0;103m"  # Yellow
On_IBlue="\033[0;104m"    # Blue
On_IPurple="\033[10;95m"  # Purple
On_ICyan="\033[0;106m"    # Cyan
On_IWhite="\033[0;107m"   # White

def AddToSeenList(art):
  global seenList, numOfSeen
  if art in seenList:
    pass
  else:
    seenList.append(art)
    numOfSeen += 1

#Creating a variable which will cause text to blink if used
Blink = "\033[5m"

#Initialising the variable which allows me to print out the menu logo
menuPrint = ("""
   _____                         
  /     \   ____   ____  __ __   
 /  \ /  \_/ __ \ /    \|  |  \\ 
/    Y    \  ___/|   |  \  |  /  
\____|__  /\___  >___|  /____/   
        \/     \/     \/       
""")  

#Initialising the variable which prints out the name of the art gallery
artGalleryPrint = ("""
   _        _       ___      _ _                         ____    _ 
  /_\  _ __| |_    / _ \__ _| | | ___ _ __ _   _  __   _|___ \  / |
 //_\\| '__| __|  / /_\/ _` | | |/ _ \ '__| | | | \ \ / / __) | | |
/  _  \ |  | |_  / /_\\ (_| | | |  __/ |  | |_| |  \ V / / __/ _| |
\_/ \_/_|   \__| \____/\__,_|_|_|\___|_|   \__, |   \_/ |_____(_)_|
                                           |___/                   
""")

#Variable which contains football ASCII art
football = ("""
          ___
      _.-'___'-._
    .'--.`   `.--'.
   /.'   \   /   `.\\
  | /'-._/```\_.-'\ |
  |/    |     |    \|
  | \ .''-._.-''. / |
   \ |     |     | /
    '.'._.-'-._.'.'
      '-:_____;-'
""")

#Variable which contains basketabll ASCII art
playingBasketball = ("""
                      =_-___
                    o    \__ \\
                   o       __| \\
                    o      \__  \\
                      oooo    \  \\
                               \  \\
 __________________             |   \\
|__________________|             \   |
 \/\/\/\/\/\/\/\/\/     _----_    |   |
  \/\/\/\/\/\/\/\/     |      \   |   |
   \/\/\/\/\/\/\/      |       |    |  |
    |/\/\/\/\/\|        |       \__/    |
    |/\/\/\/\/\|         __---          |
    |/\/\/\/\/\|       /   \            |
                      |     |          |
                      |   /            |
                      |   \            |
                      |   | \          |
                      |   |   \____-----\\
                      |   |    \____-----
                       |  |    |          \\
                       |  |   |             \\
                        \  \_|_      |       |
                         \____/  ___/ \_____/\\
                            /    /       \     \\
                          /     /          \     \\
                         /    /              \    \\
                       /    /                  \    \\
                      /   /                      \   \\
                /\   /  /                          \  |
               |  \/ \/                              \/ \\
                \    |                             __/   |
                  \_/                            /______/
""")


#Variable which contains ice hockey ASCII art
iceHockey = ("""
                    .---.
                   /_____\\
                  _HH.H.HH
   _          _-.. WHHHHHW""--__
   \\      _-"   __\VW=WV/__   /"".
    \\  _-" \__--/  "-_-"   ...    "_
     \\/ PhH  _                      ..
      \\----_/_|     ___      /"\  T""\====-
       \\ /"-._     |%|H|    (   "\|) | /  .:)
        \/     /    |-+-|     \    |_ J .:::-'
        /     /     |H|%|  _-' '-._  " )/;"
       /     / \    __    (  \ \   \   "
      /     /\/ '. /  \   \ \ \ _- \\
      "'-._/  \/  \    "-_ \ -"" _- \\
     _,'\\  \  \/  )      "-, -""    \\
  _,'_- _ \\ \  \,'          \ \_\_\  \\
,'    _-    \_\  \            \ \_\_\  \\
\_ _-   _- _,' \  \            \ ///   )
 C\_ _- _,'     \  "--------.   L_..._/
  " \/-'         "-_________|     '.-Y

""")

swimming = ("""
                      .-...-.
                     /       \\
                    ;_.-...-._;
 .,_       __,.---.-(=(o)-(o)=)-.---.,__       _,.
 '._'--"```          \   ^   /          ```"--'_.'
    ``"''~---~~%^%^.%.`._0_.'%,^%^%^~~---~''"``
jgs ~^~- `^-% ^~.%~%.^~-%-~.%-^.% ~`% ~-`%^`-~^~
       ~^- ~^- `~.^- %`~.%~-'%~^- %~^- ~^
""")

dog = ("""
    ______^ _
   |    |    \\
    \   /  ^ |
   / \_/   0  \\
  /            \\
 /    ____      0
/      /  \___ _/

""")

cat = ("""
        _..---...,""-._     ,/}/)
     .''        ,      ``..'(/-<
    /   _      {      )         \\
   ;   _ `.     `.   <         a(
 ,'   ( \  )      `.  \ __.._ .: y
(  <\_-) )'-.____...\  `._   //-'
 `. `-' /-._)))      `-._)))
   `...'         
   
""")

dolphin = ("""

                (`.              
                 \ `.           
                  )  `._..---._
\`.       __...---`         o  )
 \ `._,--'           ,    ___,'
  ) ,-._          \  )   _,-' 
 /,'    ``--.._____\/--''  

""")

camel = ("""

        _
    .--' |
   /___^ |     .--.
       ) |    /    \\
      /  |  /`      '.
     |   '-'    /     \\
     \         |      |\\
      \    /   \      /\|
       \  /'----`\   /
       |||       \\ |
       ((|        ((|
       |||        |||
      //_(       //_(

""")

drwho = ("""

        ___
_______(_@_)_______
| POLICE      BOX |
|_________________|
 | _____ | _____ |
 | |###| | |###| |
 | |###| | |###| |   
 | _____ | _____ |   
 | || || | || || |
 | ||_|| | ||_|| |  
 | _____ |$_____ |  
 | || || | || || |  
 | ||_|| | ||_|| | 
 | _____ | _____ |
 | || || | || || |   
 | ||_|| | ||_|| |         
 |       |       |        
 *****************

""")

startrek = ("""
      _____________________________________________________________
     /          _____             __   __       ___  __       ___  \\
    /          |  |  |      |\ | |  ` |  ` __ |   / |  | |  /   /   |
   /          |   |   |     | \| |    |       |  /  |  | | /   /    |
  /           |   |   |     `  ' `--' `--'    ' '   `--' '    '     |
 /     ==<===|====|====|========== U.S.S. ENTERPRISE =============  |
<_-----------|---------|--------------------------------------------|
  \__         \       /             \      \            /        /  |
     `------_  \_____/_______________\______\__________/________/__/__
           / ||  ===   ==<============ NCC-1701/7 ======--------  ===/
           \_||___________________________________________________==/
                -===-                                             -===-
""")

shaun = ("""

    ."'=-,     ,.,.,_
   (_____ )."=`      `"=,
  ./_ _  \`\             `;..
 / (o(o) |\=\              ; `;
(_/|     | \ |             ;`"`
   |     |  `             ;
   \ ..  /`,_          _.'
    `---'   `#"#""'"#'#^
             # #    # #  
             # #    # #
             # #    # #
             # #    # #
             # #    # #
            /#|#\  /#|#\\
            `"`"`  `"`"`

""")

muppets = ("""

    ___
  _(___)_
 ()'   `()          WWWWW
 .' o o `.          |o o|                 ..----..     (+)(+)
 :  _O_  :          | O |     _www_     .': o  o :`.  /      \\
 `. \_/ .'  .oo__   |(")|    /-o-o-\   .':   ()   :`. \ -==- /
  .`---'.  : -=~)) / \X/ \ (|   -   |).' :-======-: `. \    /
.' ()o() `..`--'. |   V   |  \ -=- /  `-' `.    .' `-'<\/\/\/>
:   ( \   ::    : |   |   |  /`---'\     .'      `.   /      \\
  Fozzie   Gonzo    Beaker   Scooter        Rowlf      Kermit

""")

console = ("""
   ________________
  |   |,"    `.|   | SgH
  |   /  SONY  \   |
  |O _\   />   /_  |   ___ _
  |_(_)'.____.'(_)_|  (")__(")
  [___|[=]__[=]|___]  //    \\
  
""")

sonic = ("""
          .,
.      _,'f----.._
|\ ,-'"/  |     ,'
|,_  ,--.      /
/,-. ,'`.     (_
f  o|  o|__     "`-.
,-._.,--'_ `.   _.,-`
`"' ___.,'` j,-'
  `-.__.,--'
""")

pikachu = ("""

`;-.          ___,
  `.`\_...._/`.-"`
    \        /      ,
    /()   () \    .' `-._
   |)  .    ()\  /   _.'
   \  -'-     ,; '. <
    ;.__     ,;|   > \\
   / ,    / ,  |.-'.-'
  (_/    (_/ ,;|.<`
    \    ,     ;-`
     >   \    /
    (_,-'`> .'
        (_,'

""")

croft = ("""

       ,==;,
       )a,a\g
       \=_/8
       _| (_3,
      /(__/\]\
     (_,,__) \\
     //\  ;/  \\ 
    //  )__\   \|_
  _'/  |[]__L,  ,>}
 /t}  / ,   [| 
6    /-.|=._|/
    /  .'`-/`
   ( .' | /
   \ |  ( |
    \_)  \_).
     \ \  \ |
      \ >  >|
 snd /.'  / /
         '-'

""")

#List of colours
myColours = [Red,Green,Yellow,Blue,Purple,Cyan,White,DarkCyan]

seenList = []
numOfSeen = 0

#Function which clears the screen
def ClearTheScreen():
  for i in range(80):
    print("")

#######################
## MAIN BODY OF CODE ##
#######################

#Initialising a boolean variable which will tell the program whether to loop or not
outerLoop = True

#Creating a while loop which keeps the user in the game
while(outerLoop == True):
  
  #Clearing the screen
  ClearTheScreen()
  
  #PRINTING OUT THE MENU 
  print(BRed + artGalleryPrint + END)
  print(BBlue + Blink + menuPrint + END)

  print(Green + """
╔═════════════════════════════════════════════════════════════╗
║ WELCOME to my ASCII Art Gallery!                            ║
║ We have 16 exhibits, from a variety of different categories.║
║ Enjoy...                                                    ║
╚═════════════════════════════════════════════════════════════╝ 
""" + END)
  
  print(Blue + """
  1 - Sports
  2 - Animals
  3 - Television
  4 - Video Games
  
  q - quit
  """ + END)
  
  #Asking the user to input which menu they would like to see
  menuChoice = input(Green + "Select a menu option: " + END)
  
  if(menuChoice == "q"):
    #Quitting the program
    outerLoop = False
      
  elif(menuChoice == "1"):
    #Drawing sub menu 1
    
    #Initialising variable which controls the next loop
    innerLoop1 = True
    
    #Loop which controls the sub menu
    while(innerLoop1 == True):
      
      #Clearing the screen
      ClearTheScreen()
      
      #Printing out out sub menu
      print("SUB MENU 1")
      print(Blue + '''
      1 - Football
      2 - Man Playing Basketball
      3 - Man Playing Ice Hockey
      4 - Man Swimming
      b - back to main menu
      ''' + END)
      #Asking which sub menu the user would like to visit
      menuChoice2 = input("Select a menu option: ")
      
      #Checking whether the user would like to leave the sub menu
      if(menuChoice2 == "b"):
        innerLoop1 = False
        
      #If statement which checks if the user would like to see art exhibit 1
      elif(menuChoice2 == "1"):
        #Clearing the screen
        ClearTheScreen()
        print("SPORTS EXHIBIT 1: FOOTBALL")
        #Printing out art exhibit
        print(football)
        AddToSeenList(football)

        input("Press enter to continue:")
        
      #If statement which checks if the user would like to see art exhibit 2
      elif(menuChoice2 == "2"):
        #Clearing the screen
        ClearTheScreen()
        print("SPORTS EXHIBIT 2: MAN PLAYING BASKETBALL")
        #Printing out art exhibit
        print(playingBasketball)
        AddToSeenList(playingBasketball)
        input("Press enter to continue:")

      #If statement which checks if the user would like to see art exhibit 3
      elif(menuChoice2 == "3"):
        #Clearing the screen
        ClearTheScreen()
        print("SPORTS EXHIBIT 3: MAN PLAYING ICE HOCKEY")
        #Printing out art exhibit
        print(iceHockey)
        AddToSeenList(iceHockey)
        input("Press enter to continue:")
        
      #If statement which checks if the user would like to see art exhibit 4
      elif(menuChoice2 == "4"):
        #Clearing the screen
        ClearTheScreen()
        print("SPORTS EXHIBIT 4: Man SWIMMING")
        #Printing out art exhibit
        print(swimming)
        AddToSeenList(swimming)
        input("Press enter to continue:")
        
  elif(menuChoice == "2"):
    #Drawing sub menu 2
    innerLoop2 = True
    while(innerLoop2 == True):
      
      #Clearing the screen
      ClearTheScreen()
      
      #Printing out sub menu 2
      print("SUB MENU 2")
      print(Blue + '''
      1 - Dog
      2 - Cat
      3 - Dolphin
      4 - Camel
      b - back to main menu
      ''' + END)

      menuChoice3 = input("Select a menu option: ")
      
      if(menuChoice3 == "b"):
        innerLoop2 = False
      elif(menuChoice3 == "1"):
        #Clearing the screen
        ClearTheScreen()
        print("ANIMALS EXHIBIT 1: DOG")
        #Printing out art exhibit
        print(dog)
        AddToSeenList(dog)
        input("Press enter to continue:")
        
      elif(menuChoice3 == "2"):
        #Clearing the screen
        ClearTheScreen()
        print("ANIMALS EXHIBIT 2: CAT")
        #Printing out art exhibit
        print(cat)
        AddToSeenList(cat)
        input("Press enter to continue")
        
      elif(menuChoice3 == "3"):
        #Clearing the screen
        ClearTheScreen()
        print("ANIMALS EXHIBIT 3: DOLPHIN")
        #Printing out art exhibit
        print(dolphin)
        AddToSeenList(dolphin)
        input("Press enter to continue")
        
      elif(menuChoice3 == "4"):
        #Clearing the screen
        ClearTheScreen()
        print("ANIMALS EXHIBIT 4: CAMEL")
        #Printing out art exhibit
        print(camel)
        AddToSeenList(camel)
        input("Press enter to continue")
        
  elif(menuChoice == "3"):
    #Drawing sub menu 3
    innerLoop2 = True
    while(innerLoop2 == True):
      
      #Clearing the screen
      ClearTheScreen()
      
      #Printing out sub menu 2
      print("SUB MENU 3")
      print(Blue + '''
      1 - Doctor Who Police Box
      2 - Star Trek U.S.S Enterprise
      3 - Wallace and Gromit Shaun
      4 - Muppets
      b - back to main menu
      ''' + END)

      menuChoice3 = input("Select a menu option: ")
      
      if(menuChoice3 == "b"):
        innerLoop2 = False
        
      elif(menuChoice3 == "1"):
        #Clearing the screen
        ClearTheScreen()
        print("TELEVISION EXHIBIT 1: DOCTOR WHO POLICE BOX")
        #Printing out art exhibit
        print(drwho)
        AddToSeenList(drwho)
        input("Press enter to continue:")
        
      elif(menuChoice3 == "2"):
        #Clearing the screen
        ClearTheScreen()
        print("TELEVISION EXHIBIT 2: STAR TREK U.S.S. ENTERPRISE")
        #Printint out art exhibit
        print(startrek)
        AddToSeenList(startrek)
        input("Press enter to continue")
        
      elif(menuChoice3 == "3"):
        #Clearing the screen
        ClearTheScreen()
        print("TELEVISION EXHIBIT 3: WALLACE AND GROMIT SHAUN")
        #Printint out art exhibit
        print(shaun)
        AddToSeenList(shaun)
        input("Press enter to continue")
        
      elif(menuChoice3 == "4"):
        #Clearing the screen
        ClearTheScreen()
        print("TELEVISION EXHIBIT 4: MUPPETS")
        #Printint out art exhibit
        print(muppets)
        AddToSeenList(muppets)
        input("Press enter to continue")

  elif(menuChoice == "4"):
    #Drawing sub menu 4
    innerLoop2 = True
    while(innerLoop2 == True):
      
      #Clearing the screen
      ClearTheScreen()
      
      #Printing out sub menu 4
      print("SUB MENU 4")
      print(Blue + '''
      1 - Game Console
      2 - Sonic the Hedgehog
      3 - Pikachu
      4 - Lara Croft
      b - back to main menu
      ''' + END)

      menuChoice3 = input("Select a menu option: ")
      
      if(menuChoice3 == "b"):
        innerLoop2 = False
        
      elif(menuChoice3 == "1"):
        #Clearing the screen
        ClearTheScreen()
        print("VIDEO GAMES EXHIBIT 1: GAME CONSOLE")
        #Printing out art exhibit
        print(console)
        AddToSeenList(console)
        input("Press enter to continue:")
        
      elif(menuChoice3 == "2"):
        #Clearing the screen
        ClearTheScreen()
        print("VIDEO GAMES EXHIBIT 2: SONIC THE HEDGEHOG")
        #Printint out art exhibit
        print(sonic)
        AddToSeenList(sonic)
        input("Press enter to continue")
        
      elif(menuChoice3 == "3"):
        #Clearing the screen
        ClearTheScreen()
        print("VIDEO GAMES EXHIBIT 3: PIKACHU")
        #Printint out art exhibit
        print(pikachu)
        AddToSeenList(pikachu)
        input("Press enter to continue")
        
      elif(menuChoice3 == "4"):
        #Clearing the screen
        ClearTheScreen()
        print("VIDEO GAMES EXHIBIT 4: LARA CROFT")
        #Printint out art exhibit
        print(croft)
        AddToSeenList(croft)
        input("Press enter to continue")

ClearTheScreen()
print(f"During your visit, you saw {numOfSeen} out of 16 exhibits.\n")

#Asking the user whether they would like to see a list of everything they saw in the art gallery
yesOrNo = input("Would you like to see a picture book of all the exhbits you saw? (y/n) ")

#If the user wants to see the picture book, they get their list of everything they saw
if(yesOrNo == "y"):
  for i in seenList:
    print(i)
  input("Press enter once you have finished viewing the picture book: ")
else:
  pass

#Bye in ASCII art
bye = """
 ____  _  _  ____    ____  _  _  ____  _   
(  _ \( \/ )(  __)  (  _ \( \/ )(  __)/ \\  
 ) _ ( )  /  ) _)    ) _ ( )  /  ) _) \_/  
(____/(__/  (____)  (____/(__/  (____)(_)  
"""

#Setting a frame for the bye animation
frame = 1

#Using a for loop for the animation
for i in range(6):
  #Clearing the screen before every time the colour changes
  ClearTheScreen()
  
  #Blue goodbye
  if(frame == 1):
    print(Blue + bye + END)
    frame = 2
    
  #Green goodbye
  elif(frame == 2):
    print(Green + bye + END)
    frame = 3
    
  #Red goodbye 
  elif(frame == 3):
    print(Red + bye + END)
    frame = 1
  #Sleeping for a small period of time so that the user can see the animation
  time.sleep(0.5)
