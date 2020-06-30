#Implementation of Two Player Tic-Tac-Toe game in Python.

''' A dictionary is going to be used to make the board 
    in which the number keys will be the location(i.e : top-left,mid-right,etc.)
    and initialliy it's values will be nothing and after every move 
    the value will change according to player's choice of move. '''

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
    
''' Now print the updated board after every move in the game and 
    it will make a function in which it will define the printBoard function
    so that it can easily print the board everytime by calling this function. '''

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

#main function which has all the gameplay functionality
    
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        printBoard(theBoard)
        print("It's your turn," + turn + ".Which place do you want to move to?")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That place is already taken.\nWhich place do you want to move?")
            continue
        
        #rest of the code will be added later
