#insertion sort with working out and colours
#Mr Reed - April 2024
#Now with colours and "working out"

BLUE = '\033[34m'
END = '\033[0m' 

verbose = True  # turns on and off the "work out stages of the print out"

def PrintDividedList(someList,somePos):
  if(verbose == False):
    return
  print(someList[0:somePos],end=" unsorted part -->  ")
 
  if(somePos != len(someList) - 1):
    print("[",end="")
    print(BLUE + str(someList[somePos]) + END,end = ",")
    for thing in someList[somePos+1:len(someList)-1]:
      print(str(thing),end=",")
    print(str(someList[-1]),end="]")
    print()
  else:
    print("[" + BLUE + str(someList[somePos]) + END,end = "]")
  input()

def InsertionSortTheList(aList):
 
  #The list is printed several times during this process with a clear indication where the split is
  #between the sorted and unsorted parts of the list
 
  for i in range(1,len(aList)):
   
    PrintDividedList(aList,i)
   
    pos = i
    currentItem = aList[i]
   
    while(pos > 0 and aList[pos-1] > currentItem):
      #move big item one place right
      aList[pos] = aList[pos-1]
      pos = pos -1
     
    #found where this item goes in the left part of the list
    aList[pos]= currentItem

# main program
alist = [2,1,15,5,4,3,5,8,11,123]
print("Initial list")
print(alist)
print()
input()
InsertionSortTheList(alist)
print("\n\nSorted list")
print(alist)
