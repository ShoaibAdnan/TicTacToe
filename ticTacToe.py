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