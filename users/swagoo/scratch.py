weapons = ["rock", "paper", "scissors"]

player1 = int(input("player 1: "))
player2 = int(input("player 2: "))

if player1 == player2:
    winner = "Draw"
else:
    winner = "Player 1 wins!" if player1 == (player2 + 1) % 3 else "Player 2 wins!"

print(winner)