import random

player1 = input("slect Rock, paper, or Scissor :").lower()
player2 = random.choice(["Rock", "Paper", "Scissor"]).lower()
print("player 2 selected: ", player2)

if player1 == "rock" and player2 == "paper":
    print("player 2 won")
elif player1 == "paper" and player2 == "scissor":
    print("player 2 won")
elif  player1 == "scissor" and player2 == "rock":
    print("player 2 won")
elif  player1 == player2:
    print("Tie")
else:
    print("You Won")           