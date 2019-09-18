#! /usr/bin/python3.6


def main():
    # Dictionary to store the positions occupied along with the number
    print("Welcome to the Game!")
    play = 1
    while(play == 1):
        play_game()
        print("Enter 1 to play another game and 0 to exit");
        play = input()
        play = int(play)

# Function to check if sum of any complete row, column or diagonal has become 15
def check(game):
    finish = 0
    h1 = 0
    h2 = 0
    h3 = 0
    v1 = 0
    v2 = 0
    v3 = 0
    d1 = 0
    d2 = 0

    # Calculate sum in row 1 when filled completely
    if( (1 in game.keys()) and (2 in game.keys()) and (3 in game.keys())):
        h1 = game[1] + game[2] + game[3]
    
    # Calculate sum in row 2 when filled completely
    if( (4 in game.keys()) and (5 in game.keys()) and (6 in game.keys())):
        h2 = game[4] + game[5] + game[6]
    
    # Calculate sum in row 3 when filled completely
    if( (7 in game.keys()) and (8 in game.keys()) and (9 in game.keys())):
        h3 = game[7] + game[8] + game[9]
    
    # Calculate sum in col 1 when filled completely
    if( (1 in game.keys()) and (4 in game.keys()) and (7 in game.keys())):
        v1 = game[1] + game[4] + game[7]
    
    # Calculate sum in col 2 when filled completely
    if( (2 in game.keys()) and (5 in game.keys()) and (8 in game.keys())):
        v2 = game[2] + game[5] + game[8]
    
    # Calculate sum in col 3 when filled completely
    if( (3 in game.keys()) and (6 in game.keys()) and (9 in game.keys())):
        v3 = game[3] + game[6] + game[9]
    
    # Calculate sum in diagonal 1 when filled completely
    if( (1 in game.keys()) and (5 in game.keys()) and (9 in game.keys())):
        d1 = game[1] + game[5] + game[9]

    # Calculate sum in diagonal 2 when filled completely    
    if( (3 in game.keys()) and (5 in game.keys()) and (7 in game.keys())):
        d2 = game[3] + game[5] + game[7]
    
    #Check if any of the sum is 15
    if( h1 == 15 or h2 == 15 or h3 == 15 or v1 == 15 or v2 == 15 or v3 == 15 or d1 == 15 or d2 == 15):
        finish = 1
    
    # Return 1 if sum has reached 15 and 0 otherwise
    return finish

# Function to display the game status
def disp(game):
    c = {}
    for i in range(1,10):
        if(i in game.keys()):
            c[i] = game[i]
        else:
            c[i] = 0
        
    print(c[1],c[2],c[3])
    print(c[4],c[5],c[6])
    print(c[7],c[8],c[9])

# function to play the game
def play_game():
    chance = 1
    exit = 0
    player = 1
    flg = 0    
    game = {}
# Maximum 9 chances possible since there are 9 positions
# Exit is made 1 when the game ends after wining or when all the positions are occupied

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

        # Boundary Condition Check
        if((p < 1) or ( p > 9)):
            print("Invalid Position")
            flg = 1

        if((n < 1) or ( n > 9)):
            print("Invalid Number")
            flg = 1

        if( n in game.values()):
            print("Number already used")
            flg = 1

        if( p in game.keys()):
            print("Position already occupied")
            flg = 1
    
        if((player == 1 and n%2 != 1) or (player == 2 and n%2 != 0)):
            if(player%2 == 1):
                print("Even number used")
            if(player%2 == 0):
                print("Odd number used")
            flg = 1

        # Loop till correct input is entered
        while(flg == 1):
            print("Please enter the correct position and number")
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
            elif( p in game.keys()):
                print("Position already occupied")
                flg = 1
            elif((player == 1 and n%2 != 1) or (player == 0 and n%2 != 0)):
                if(player%2 == 1):
                    print("Even number used")
                if(player%2 == 0):
                    print("Odd number used")
                flg = 1
            else:
                flg = 0

        # Add position and number in the dictionary
        game[p] = n
    
        disp(game)

        # Call function to check if sum has reached 15 and declare the winner
        if(check(game) == 1):
            print("Player",player,"Wins!")
            exit = 1
            print("End of the Game!")  
        elif (len(game) == 9):
            print("It's a Draw")
            print("End of the Game!")
            exit = 1
        chance += 1   


# Calling the main function to start execution of program
main()
