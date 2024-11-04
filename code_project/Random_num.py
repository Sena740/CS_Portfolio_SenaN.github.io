#Number Guessing Game
#2024/09/18 By Sena Nishimura
import random #importing random allows us to generate random numbers for this game

def right(): #allows the user to replay or end the game when guessed correctly
    print("You guessed correct!\nTry again? (Y/N)")
    confirm = input()
    if confirm == "y":
        difficulty()
    elif confirm == "n":
        print("Thank you for playing!")

def wrong(): #allows the user to replay or end the game when guessed incorrectly
    print("You ran out of guesses!\nTry again? (Y/N)")
    confirm = input()
    if confirm == "y":
        difficulty()
    elif confirm == "n":
        print("Thank you for playing!")

#easy mode with a number range of 1 to 10, and 5 guesses
def easy():
    counter = int(5)
    correct = 0
    num = int(random.randrange(1,10)) #chooses a number within the range
    print("Range is 1 to 10, you have",counter,"guesses left")
    while(counter >= 1): #runs while the user has guesses remaining
        guess = int(input())
        if guess > num: #tells the user that the number they guessed were too high
            counter = counter - 1
            print("Too High!", counter, "guesses left")
        elif guess < num: #tells the user that the number they guessed were too low
            counter = counter - 1
            print("Too Low!", counter, "guesses left")
        elif guess == num:
            counter = 0
            correct = 1
    if counter == 0: #wether right or wrong, allows the user to replay or quit the game
        if correct == 1:
            right()
        if correct == 0:
            wrong()

#medium mode with a number range of 1 to 100, and 4 guesses
def medium(): #works the same as the easy function, just different number range and guess count
    counter = int(4)
    correct = 0
    num = int(random.randrange(1,100))
    print("Range is 1 to 100, you have",counter,"guesses left")
    while(counter >= 1):
        guess = int(input())
        if guess > num:
            counter = counter - 1
            print("Too High!", counter, "guesses left")
        elif guess < num:
            counter = counter - 1
            print("Too Low!", counter, "guesses left")
        elif guess == num:
            counter = 0
            correct = 1
    if counter == 0:
        if correct == 1:
            right()
        if correct == 0:
            wrong()
#hard mode with a number range of 1 to 1000, and 3 guesses
def hard(): #works the same as the easy function, just different number range and guess count
    counter = int(3)
    correct = 0
    num = int(random.randrange(1,1000))
    print("Range is 1 to 1000, you have",counter,"guesses left")
    while(counter >= 1):
        guess = int(input())
        if guess > num:
            counter = counter - 1
            print("Too High!", counter, "guesses left")
        elif guess < num:
            counter = counter - 1
            print("Too Low!", counter, "guesses left")
        elif guess == num:
            counter = 0
            correct = 1
    if counter == 0:
        if correct == 1:
            right()
        if correct == 0:
            wrong()

def difficulty(): #allows the user to select the difficulty for this game
    print("Please select the difficulty: \n| Easy | Medium | Hard |") #asks the user to choose an difficulty
    dif = input()
    if dif == "easy": #initiate the easy function when the user types easy
        easy()
    elif dif == "medium": #initiate the medium function when the user types medium
        medium()
    elif dif == "hard": #initiate the hard function when the user types hard
        hard()
    else:
        print("Invalid option") #typing anything other tha three options prompts the selection again
        difficulty()

difficulty()