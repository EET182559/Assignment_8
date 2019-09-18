#! /usr/bin/python3.6

game = {}
print("Welcome to the Game!")

chance = 1
exit = 0
player = 1
h1 = 0
h2 = 0
h3 = 0
v1 = 0
v2 = 0
v3 = 0
d1 = 0
d2 = 0
flg = 0

while(exit == 0 and chance < 10):
    if(chance%2 == 1): 
        print("Player 1")   
        player = 1
    if(chance%2 == 0): 
        print("Player 2")   
        player = 2
    print("Enter the position and number to be entered: ")
    p,n = input().split(',')
    p = int(p)
    n = int(n)
    if((p < 1) or ( p > 9)):
        print("Invalid Position")
        flg = 1

    if((n < 1) or ( n > 9)):
        print("Invalid Number")
        flg = 1

    if( n in game.values()):
        print("Number already used")
        flg = 1

    while(flg == 1):
        print("Please re-enter the position and number")
        p,n = input().split(',')
        p = int(p)
        n = int(n)
        if((p < 1) or ( p > 9)):
            print("Invalid Position")
            flg = 1
        elif((n < 1) or ( n > 9)):
            print("Invalid Number")
            flg = 1
        elif( n in game.values()):
            print("Number already used")
            flg = 1
        else:
            flg = 0

    game[p] = n
    if( (1 in game.keys()) and (2 in game.keys()) and (3 in game.keys())):
        h1 = game[1] + game[2] + game[3]
    if( (4 in game.keys()) and (5 in game.keys()) and (6 in game.keys())):
        h2 = game[4] + game[5] + game[6]
    if( (7 in game.keys()) and (8 in game.keys()) and (9 in game.keys())):
        h3 = game[7] + game[8] + game[9]
    if( (1 in game.keys()) and (4 in game.keys()) and (7 in game.keys())):
        v1 = game[1] + game[4] + game[7]
    if( (2 in game.keys()) and (5 in game.keys()) and (8 in game.keys())):
        v2 = game[2] + game[5] + game[8]
    if( (3 in game.keys()) and (6 in game.keys()) and (9 in game.keys())):
        v3 = game[3] + game[6] + game[9]
    if( (1 in game.keys()) and (5 in game.keys()) and (9 in game.keys())):
        d1 = game[1] + game[5] + game[9]
    if( (3 in game.keys()) and (5 in game.keys()) and (7 in game.keys())):
        d2 = game[3] + game[5] + game[7]
    if( h1 == 15 or h2 == 15 or h3 == 15 or v1 == 15 or v2 == 15 or v3 == 15 or d1 == 15 or d2 == 15):
        print("Player",player,"Wins!")
        exit = 1
        print("End of the Game!")  
    elif (len(game) == 9):
        print("End of the Game!")
        exit = 1
    chance += 1    
