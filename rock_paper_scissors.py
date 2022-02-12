import random

user_wins = 0
computer_wins = 0

options = ["ROCK", "PAPER", "SCISSORS"]

while True:
    # set user choice
    user = input("Type Rock, Paper, Scissors. Or hit 'q' to quit: ")
    user = user.upper()
    # set computer choice
    random_num = random.randint(0,2)
    computer = options[random_num]

    if user == "Q":
        break
    if user not in options:
        continue

    print("You picked", user)
    print("Computer picked", computer)

    # check outcomes
    if user == computer:
        print("Draw")
    elif user == "ROCK":
        if computer == "SCISSORS":
            print("Rock beats Scissors, you win!")
            user_wins+=1
        else:
            print("Paper beats Rock, you lose!")
            computer_wins+=1
    elif user == "PAPER":
        if computer == "ROCK":
            print("Paper beats Rock, you win!")
            user_wins+=1
        else:
            print("Scissors beats Paper, you lose!")
            computer_wins+=1
    elif user == "SCISSORS":
        if computer == "Paper":
            print("Scissors beats Paper, you win!")
            user_wins+=1
        else:
            print("Rock beats Scissors, you lose!")
            computer_wins+=1

print("You won",user_wins,"times")
print("Computer won",computer_wins,"times")
print("Goodbye!")