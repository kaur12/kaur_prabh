from random import randint

#  available weapons => store this in an array
choises = ["Rock", "Paper", "Scissors"]
player = False

computer_lives = "3"
player_lives = "3"

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
            player_lives == "player_lives - 1"
        else:
            print("You win!", player, "smahes", computer)
            computer_lives == "computer_lives - 1"

    elif player == "Paper":
        if computer == "Scissors":
            print("You lose!", computere, "cuts", player)
            player_lives == "player_live - 1"
        else:
            print("You win!", player, "covers", computer)
            computer_lives == "computer_lives - 1"

    elif player == "Scissors":
        if computer =="Rock":
            print("You lose!", computer, "smashes", player)
            player_lives == "player_lives - 1"
        else:
            print("You win!", player, "cuts", computer)
            computer_lives == "computer_lives - 1"

    elif player =="Quit":
        exit()
    if lives =="0":
        play_again = input("Play again?")
        while play_again not in ("Yes","No"):  # validate user input
            print("Please try again")
            play_again = input("Play again?")
        if play_again == "No":
            print("Game Over")
            continue_playing = False
        # Don't return here (you returned the input), I really don't think that what you wanted

        print("Not a valid option. Check again, and check you spelling\n")

    player = False
    computer = choises[randint(0, 2)]