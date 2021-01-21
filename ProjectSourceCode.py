Guessing = 0

while (True):
  int1=int(input("Guse a number :"))
  Guessing = Guessing+1
  
  #Condition
  if Guessing==6:
    print("You lose !!")
    print("You use ",Guessing,"guse")
    break
  
  if int1>9:
    print("NO !! guse number under" ,int1)
  elif int1<9:
    print("NO !! guse number upto" ,int1)
  elif int1==9:
    print("Congratulation !! You won the game by useing",Guessing,"guse")
    break
