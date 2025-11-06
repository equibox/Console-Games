from random import randint

print("Welcome to Number Guesser")

numToGuess = randint(1, 100)
tries = 0

while True:
    #print(numToGuess)
    numGuessed = int(input("Guess a number 1-100: "))
    tries += 1
    if numGuessed > 100 or numGuessed < 0:
        print("Invalid number")
        continue
    if numGuessed > numToGuess:
        print("Too high.")
        continue
    elif numGuessed < numToGuess:
        print("Too low.")
        continue
    elif numGuessed == numToGuess:
        print("Correct!")
        print("Tries:", tries)
        exit()