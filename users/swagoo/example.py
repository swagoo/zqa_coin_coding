import random


def scoreboard(win, loss, draw):
    print(f"Player 1 wins: {win}\nPlayer 2 wins: {loss}\ndraws: {draw}")




#change this to be input into string not int
def player_input(player_num):

    players_pick = input(f"""Player {player_num}: please select a number: (0) rock, (1) paper, (2) scissors, (4) restart, (5) quit. 
    >""")
    while not players_pick.isdigit() or int(players_pick) not in list(range(0, 6)):
        print("Invalid input. Please enter a valid number.")
        players_pick = input(f"""Player {player_num}: please select a number: (0) rock, (1) paper, (2) scissors, (4) restart, (5) quit. 
    >""")
    return int(players_pick)
        

weapons = ["rock", "paper", "scissors"]

def rock_paper_scissors():

    win = 0
    loss = 0
    draw = 0



    player_select = input("Single player or multiplayer?").lower()

    while True:

        if player_select == "multiplayer":
            playerchoice1 = player_input(1)
            playerchoice2 = player_input(2)
        else:
            playerchoice1 = player_input(1)
            playerchoice2 = random.randrange(0, 3)

        if playerchoice1 == 4:
            print("restart")
            win = 0
            loss = 0
            draw = 0
            player_select = input("Single player or multiplayer? ").lower()

        elif playerchoice1 == 5:
            print("I knew you were soft...")
            break

        if playerchoice1 == playerchoice2:
            winner = "Draw"
            draw += 1
        
        #can combine line 61 -> 64 into this ternary 
        else:
            winner = "Player 1 wins!" if playerchoice1 == (playerchoice2 + 1) % 3 else "Player 2 wins!"
            
        print(winner)
        
        if winner == "Player 1 wins!":
            win += 1
        elif winner == "Player 2 wins!":
            loss += 1


        scoreboard(win, loss, draw)
        
       
        
#################################################################################################################


play = input("Do you want to play a game you sicko? ").lower()

if play == "yes":
    rock_paper_scissors()
else:
    print("I didn't want to play either.")
