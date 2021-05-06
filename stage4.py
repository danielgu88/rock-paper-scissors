import random

ratings = {}
score = 0
WIN_CHANGE = 100
DRAW_CHANGE = 50


def computer_move(input_):
    global score
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
            score += DRAW_CHANGE
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))
            score += WIN_CHANGE
    elif computer_move == "paper":
        if input_ == "rock":
            print("Sorry, but the computer chose {}".format(computer_move))
        elif input_ == "paper":
            print("There is a draw ({})".format(computer_move))
            score += DRAW_CHANGE
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))
            score += WIN_CHANGE
    else:
        if input_ == "paper":
            print("Sorry, but the computer chose {}".format(computer_move))
        elif input_ == "scissors":
            print("There is a draw ({})".format(computer_move))
            score += DRAW_CHANGE
        else:
            print("Well done. The computer chose {} and failed".format(computer_move))
            score += WIN_CHANGE


random.seed()
name = input("Enter your name: ")
print("Hello,", name)

file = open("rating.txt", "r")

for line in file:
    current_line = line.split(" ")
    ratings[current_line[0]] = int(current_line[1].rstrip("\n"))

file.close()

if name in ratings:
    score = ratings[name]

input_ = ""

while True:
    input_ = input()

    if input_ in ["rock", "paper", "scissors"]:
        computer_move(input_)
    elif input_ == "!exit":
        break
    elif input_ == "!rating":
        print("Your rating: {}".format(score))
    else:
        print("Invalid input")

print("Bye!")
