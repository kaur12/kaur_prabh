from random import randint

#  available weapons => store this in an array
choises = ["Rock", "Paper", "Scissors"]
player = False

# make the computer pick one item at random
computer = choises[randint(0, 2)]

# show the computer's choise in the terminal window
print("Computer chooses: ", computer)

while player is False:
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    # check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif (player == "Rock"):
        if computer == "Paper":
            #computer won
            print("You lose", computer, "covers", player)
        else:
            print("You win!", player, "smahes", computer)

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computere, "cuts", player)
        else:
            print("You win!", player, "covers", computer)

    elif player == "Scissors":
        if computer =="Rock":
            print("You lose!", computer, "smashes", player)
        else:
            print("You win!", player, "cuts", computer)

    elif player =="Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check you spelling\n")

    player = False
    computer = choises[randint(0, 2)]