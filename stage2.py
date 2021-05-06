import random


def computer_move(input_):
    random_number = random.randint(0, 2)
    computer_move = ""

    if random_number == 0:
        computer_move = "rock"
    elif random_number == 1:
        computer_move = "paper"
    else:
        computer_move = "scissors"

    if computer_move == "rock":
        if input_ == "scissors":
            print("Sorry, but the computer chose {}".format(computer_move))
        elif input_ == "rock":
            print("There is a draw ({})".format(computer_move))
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))
    elif computer_move == "paper":
        if input_ == "rock":
            print("Sorry, but the computer chose {}".format(computer_move))
        elif input_ == "paper":
            print("There is a draw ({})".format(computer_move))
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))
    else:
        if input_ == "paper":
            print("Sorry, but the computer chose {}".format(computer_move))
        elif input_ == "scissors":
            print("There is a draw ({})".format(computer_move))
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))


random.seed()
input_ = input()

computer_move(input_)
