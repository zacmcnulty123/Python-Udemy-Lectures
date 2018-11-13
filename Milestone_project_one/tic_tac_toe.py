import csv
import sys
def display_board(myInput, playerInput, lst):
    if not (myInput - 1) in range(1,9):
        print('Please select a valid input')
        return lst
    if not lst[myInput-1] == ' ':
        print('Please select a different tile')
        return lst
    else:
        lst[myInput-1] = playerInput
        board = ('    |    |    \n'
                '  {} | {}  | {} \n'
                +'    |    |    \n'
                +'--------------\n'
                +'    |    |    \n'
               +'  {} | {}  | {} \n'
                +'    |    |    \n'
                +'--------------\n'
                +'    |    |    \n'
               +'  {} | {}  | {} \n'
                +'    |    |    \n').format(lst[6], lst[7], lst[8], lst[3],
                                      lst[4], lst[5], lst[0], lst[1], lst[2])
    print(board)
    return lst
def player_turn(lst, playerChar):
    playerInput = input('Please select a number between 1-9 for the spot on the board:\t')
    lst = display_board(int(playerInput), playerChar, lst)
    return lst
def check_win(lst, playerChar):
    if (lst[0] + lst[1] + lst[2] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[3] + lst[4] + lst[5] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[6] + lst[7] + lst[8] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[0] + lst[3] + lst[6] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[1] + lst[4] + lst[7] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[2] + lst[5] + lst[8] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[0] + lst[4] + lst[8] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    elif(lst[2] + lst[4] + lst[6] == playerChar+playerChar+playerChar):
        print('You have won the game')
        return True
    else:
        return False
    return 
def game_start():
    playerChar = input('Player 1 would you like to be X or O?\t')
    playerChar = playerChar.upper()
    lst = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    while not check_win(lst, playerChar):
        lst = player_turn(lst, playerChar)
        if playerChar == 'X':
            playerChar = 'O'
        else:
            playerChar = 'X'
    return
def replay():
    replay = input('Would you like to play again? Yes or No')
    if replay.lower() == 'yes':
        return False
    else:
        return True
game_start()
while not replay():
    game_start()