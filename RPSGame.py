from random import randint

#  available weapons => store this in an array
choises = ["Rock", "Paper", "Scissors"]
player = False

computer_lives = 5
player_lives = 5

# make the computer pick one item at random
computer = choises[randint(0, 2)]


#define a win or lose function instead of the procedural way
def winorlose(status):
    #handle win or lose based on the status we pass in
    print("Called the win or lose fuunction")
    print("***********************")
    print("You", status, "!", "Would you like to play again?")
    choice = input("Y / N:")

    if choice == "Y" or choice =="y":
        #reset the game
        ##change global variables
        global player_lives
        global computer_lives
        global player
        global computer

        computer_lives = 5
        player_lives = 5
        player = False
        computer = choises[randint(0,2)]

    elif choice == "N" or choice =="n":
        print("You choose to quit")
        exit()

# show the computer's choise in the terminal window
print("Computer chooses: ", computer)

while player is False:
    print("****************************************")
    print("player_lives:", player_lives, "/5")
    print("AI_lives:", computer_lives, "/5")
    print("****************************************")
    player = input("Rock, Paper or Scissors?\n")
    print("Player chooses:", player)

    # check to see if you picked the same thing
    if (player == computer):
        print("Tie! Live to shoot another day")

    elif (player == "Rock"):
        if computer == "Paper":
            #computer won
            player_lives -= 1
            print("You lose", computer, "covers", player, "\n")
        else:
            print("You win!", player, "smahes", computer, "\n")
            computer_lives -= 1

    elif player == "Paper":
        if computer == "Scissors":
            player_lives -= 1
            print("You lose!", computer, "cuts", player, "\n")
        else:
            print("You win!", player, "covers", computer, "\n")
            computer_lives -= 1

    elif player == "Scissors":
        if computer =="Rock":
            player_lives -= 1
            print("You lose!", computer, "smashes", player, "\n")
        else:
            print("You win!", player, "cuts", computer, "\n")
            computer_lives -= 1

    elif player =="Quit":
        exit()

    else:
        print("Not a valid option. Check again, and check you spelling\n")

    #handle win or lose
    if player_lives is 0:
        winorlose("lost")

    elif computer_lives is 0:
        winorlose("won")        

    player = False
    computer = choises[randint(0, 2)]