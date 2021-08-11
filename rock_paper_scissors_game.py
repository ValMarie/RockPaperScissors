import random

def play():
    user = input("What's your choice rock 'r', paper 'p' or scissors 's'?\n " )
    computer = random.choice(["r", "p", "s"])

    if user == computer:
        print("It's a tie")

    elif is_win (user, computer):
        return "You won"
       
    return "You lost"

# p beats r, r beats s and s beats p
def is_win(player, opponent):
    if player == "p" and opponent == "r" or player == "r" and opponent == "s" or player == "s" and opponent == "p":
        return True

while True:
    print(play())