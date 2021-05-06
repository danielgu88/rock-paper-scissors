def computer_move(input_):
    if input_ == "rock":
        return "paper"
    elif input_ == "paper":
        return "scissors"
    elif input_ == "scissors":
        return "rock"


input_ = input()

print("Sorry, but the computer chose", computer_move(input_))
