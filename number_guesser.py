from pickle import TRUE
import random

top_number = input("Enter a number greater than 0: ")
if top_number.isdigit():
    top_number = int(top_number)

    if top_number <= 0:
        print("Start again and enter a number greater than 0")
        quit()

else:
    print("Start again and enter a number")
    quit()

random_number = random.randint(0,top_number)

guesses = 1

while TRUE:
    guesses+=1
    guess = input("Make a guess: ")
    if guess.isdigit():
        guess = int(guess)

        if guess == random_number:
            if guesses == 1:
                print("Correct! You got it in 1 go!")
                break
            else:
                print("Correct! You got it in", guesses, "guesses.")
                break
        elif guess > random_number:
            print("Too high")
        else:
            print("Too low")
           
    else:
        print("Enter a number")