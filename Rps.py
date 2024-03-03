import random
import os
import pyfiglet
import time
import progressbar

output = pyfiglet.figlet_format("Dr.ele11ven")
print(output)
bar = progressbar.ProgressBar(maxval=20, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
bar.start()
for i in range(20):
    bar.update(i+1)
    time.sleep(0.2)
bar.finish()



def compare_moves(my_move, opponent_move):
    # Compare the moves and return the result
    if my_move == opponent_move:
        return "It's a tie!"
    elif (my_move == "rock" and opponent_move == "scissors") or \
         (my_move == "scissors" and opponent_move == "paper") or \
         (my_move == "paper" and opponent_move == "rock"):
        return "We won!"
    else:
        return "We lost!"

def always_win_rps(opponent_move):
    # If we lost the previous round, choose the shape that beats the opponent's move
    if previous_move == "rock" and opponent_move == "scissors":
        return "paper"
    elif previous_move == "scissors" and opponent_move == "paper":
        return "rock"
    elif previous_move == "paper" and opponent_move == "rock":
        return "scissors"

    # If we won the previous round, choose the shape that lost to the opponent's move
    elif previous_move == "rock" and opponent_move == "paper":
        return "scissors"
    elif previous_move == "scissors" and opponent_move == "rock":
        return "paper"
    elif previous_move == "paper" and opponent_move == "scissors":
        return "rock"

    # If it's the first round or it's a tie, choose the shape randomly
    else:
        return random.choice(["rock", "paper", "scissors"])

os.system('cls')
output = pyfiglet.figlet_format("Rock, Paper, Scissors Game")

print ('===========================================')
print(output)

print ('===========================================')
# Initialize variables
previous_move = None
opponent_move = input("Enter your move to start (rock, paper, scissors): ")
tie =0
lost=0
win=0
os.system('cls')

while True:
    

    
    print(output)
    print ('===========================================')
    print ('Rock, Paper, Scissors Game')
    
    print ('===========================================')
    print("user move : "+opponent_move)
    
    print ('===========================================')
    
    
    # Make our move based on the algorithm
    move = always_win_rps(opponent_move)

    # Print our move
    print(f"Our move: {move}")

    # Get the result of the round
    result = compare_moves(move, opponent_move)
    if result == "It's a tie!":
        tie += 1
    elif result == "We won!":
        win += 1
    elif result == "We lost!":
        lost += 1
    
    print(f"User losses: {win}, Ties: {tie}, User win: {lost}")


    # Update the previous move
    previous_move = move

    # Get the opponent's move for the next round
    opponent_move = input("Enter your move (rock, paper, scissors): ")

    os.system('cls')
    

    

