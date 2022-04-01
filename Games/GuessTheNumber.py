# Guess the number game!

import random

def GetName():
    while True:
        name = input()
        if len(name) > 1:
            return name
        print("That name is too short for me to deal with! Please enter your name.")

def GetNum():
    while True:
        try:
            num = int(input())
            if num >= 1:
                return num
            else:
                print("please enter a number larger than 0")
        except:
            print("Please enter a posive value larger than 0 using the following format: 1234")

def GetGuessCount(maxNum):
    guessCount = 1
    square = 2

    while square < maxNum:
        square = square * 2
        guessCount = guessCount + 1
    return guessCount

def PlayGame():
    print("How high would you like the guessing game number to be?")
    maxNum = GetNum()
    guessCount = GetGuessCount(maxNum)
    print("Wow! I'm going to give you " + str(guessCount) + " tries to guess my number. Are you Ready?")

    secretNumber = random.randint(1, maxNum)

    print("Guess a number!")

    for guessNumber in range(1, guessCount + 1):
        guess = GetNum()
        if guess == secretNumber:
            print("You guessed it! You guessed my number in only " + str(guessNumber) + " tries!")
            break;
        elif guess < secretNumber:
            print("Too Low... ", end='')
        else:
            print("Too high... ", end='')

        if guessCount - guessNumber > 0:
            print("Guess again! You have " + str(guessCount - guessNumber) + " guesses left!")
        else:
            print("You ran out of guesses! The number I was thinking of was " + str(secretNumber) + "!")

def GetPlayAgainResponse():
    print("Want to play again? (y/n)")
    while True:
        choice = input()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Please enter 'y' or 'n':")


print("Hello! What is your name?")
name = GetName()
print("Hi "+name+".", end=' ')

playing = True;
while playing:
    PlayGame()
    playAgain = GetPlayAgainResponse()
    playing = playAgain

