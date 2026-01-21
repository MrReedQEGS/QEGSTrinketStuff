#STARTING POINT for the beginning of a naughts and crosses game
#
#  1 2 3
#  4 5 6
#  6 7 9
#

possibleValues = ["X","O"," "]

#Blank the whole board
pos1 = possibleValues[2]
pos2 = possibleValues[2]
pos3 = possibleValues[2]
pos4 = possibleValues[2]
pos5 = possibleValues[2]
pos6 = possibleValues[2]
pos7 = possibleValues[2]
pos8 = possibleValues[2]
pos9 = possibleValues[2]

#Data structure for the game board
board = [[pos1,pos2,pos3],
         [pos4,pos5,pos6],
         [pos7,pos8,pos9]]

#Code to draw the current game board
def Horizontal():
  print("-------------")

def DisplayBoard():
  
  Horizontal()
  for i in range (3):
    print("| ",end="")
    for j in range (3):
      print(board[i][j],end=" | ")
    print("")
    Horizontal()

#MAIN BODY
DisplayBoard()

#Your job is to write the actual game!
