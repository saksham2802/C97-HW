import random

from numpy import compare_chararrays 
correctAnswer=random.randint(1,10)
gameOver=False

while gameOver==False:
    playerGuess=int(input("Enter a number between 1-10    "))

    if playerGuess==correctAnswer:
        compareAnswer ="Correct"
        gameOver=True

    elif playerGuess>correctAnswer:
        compareAnswer="Lower No "
    
    elif playerGuess<correctAnswer:
        compareAnswer="Higher No"

    if compareAnswer=="Correct":
        print("You guessed Correctly")
    
    elif compareAnswer=="Lower No":
          print("Enter a lower Number")
    
    elif compareAnswer=="Higher No":
        print("Enter a higher Number")
