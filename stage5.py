import random

ratings = {}
score = 0
WIN_CHANGE = 100
DRAW_CHANGE = 50
moves = ["rock", "paper", "scissors"]


# Computer's move
def computer_move(input_):
    global score
    index = random.randint(0, len(moves) - 1)
    computer_move = moves[index]
    result = ""

    new_list = moves[index + 1:len(moves)] + moves[0:index]
    winning_moves = new_list[0:int(len(new_list) / 2)]
    losing_moves = new_list[int(len(new_list) / 2):len(new_list)]

    if input_ in winning_moves:
        result = "win"
    elif input_ in losing_moves:
        result = "lose"
    else:
        result = "draw"

    if result == "win":  # User wins
        print("Well done. The computer chose {} and failed".format(computer_move))
        score += WIN_CHANGE
    elif result == "draw":  # User ties
        print("There is a draw ({})".format(computer_move))
        score += DRAW_CHANGE
    else:  # User loses
        print("Sorry, but the computer chose {}".format(computer_move))


random.seed()

# Prompt for name
name = input("Enter your name: ")
print("Hello,", name)

# Check rating.txt
file = open("rating.txt", "r")
for line in file:
    current_line = line.split(" ")
    ratings[current_line[0]] = int(current_line[1].rstrip("\n"))

file.close()

if name in ratings:
    score = ratings[name]

# Prompt for moves
move_input = input()

if move_input != "":
    moves = move_input.split(",")

print("Okay, let's start")

input_ = ""

while True:
    input_ = input()

    if input_ in moves:
        computer_move(input_)
    elif input_ == "!exit":
        break
    elif input_ == "!rating":
        print("Your rating: {}".format(score))
    else:
        print("Invalid input")

print("Bye!")
