# 1. Name:
#      Brighton Roskelley
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      This program allows the user to place values in a board 
#      playing sudoku with the rules coded in.
# 4. What was the hardest part? Be as specific as possible.
#      I struggled with getting my check functions to work with both my 
#      show possible functions and edit board function
# 5. How long did it take for you to complete the assignment?
#      This took me about 3.5 hours

import json


def read_board():
    file_name = input('What is the filename? ')

    with open("131.05.Easy.json", "r") as file:
        json_text = file.read()
        board_json = json.loads(json_text)
    return board_json['board']

def save_board(file_name,board):
    with open(file_name,"w") as file:
        board_json = {}
        board_json['board'] = board
        board_text = json.dumps(board_json)
        file.write(board_text)

def display_board(board):
    print ("   A B C D E F G H I")
    for row in range(9):
        if row == 3 or row == 6:
            print ("  ------+-----+-----")
        print (row + 1, " ", end='')

        for column in range(9):
            separator = [' ', ' ','|', ' ', ' ','|',' ', ' ','\n']
            print(board[row][column] if board[row][column] != 0 else ' ',
                end=separator[column])

def get_user_square():
    valid_input = False
    while not valid_input:
        print("what square would you like to edit?")
        sqr_value = input(">")
        if sqr_value == "s":
            valid_input = True
            sqr_coord = "s"
        else:
            sqr_coord = []
            sqr_coord = set_square_coords(sqr_value)
            valid_input = sqr_coord[2]
    return sqr_coord

def set_square_coords(sqr_value):
    row = -1
    column = -1
    for letter in sqr_value.lower():
        
        if 'a' <= letter <= 'i':
            column = ord(letter)-ord('a')
        if '1' <= letter <= '9':
            row = int(letter) - 1 
            
    
    return [row , column , True if row != -1 and column != -1 else False]


def get_input_value():
    is_valid = True
    while is_valid:
        print("what value do you want to place on the board?")
        user_value = input(">")
        is_valid = check_valid_value(user_value)
    
    return user_value

def check_valid_value(user_value):
    
    if user_value.lower() == "s":
        is_valid = False
    elif user_value.lower() == "q":
        is_valid = False
    elif 1 <= int(user_value) <= 9:
        is_valid = False
    else:
        is_valid = True

    return is_valid

def update_board(board,user_square,user_input_value):
    is_legal = determine_avalable(user_square,board, user_input_value)
    row = user_square[1]
    column = user_square[0]
    if is_legal == False:
        print("That is not a legal move.")
    else:
        board[column][row] = user_input_value

    return board

def determine_avalable(sqr_coord, board, user_input_value):
    is_legal = check_column(sqr_coord, board, int(user_input_value))
    if is_legal:
        is_legal = check_row(sqr_coord, board, int(user_input_value))
    if is_legal:
        is_legal = check_box(sqr_coord, board, int(user_input_value))
    return is_legal


def show_available_values(sqr_coord,board):
    available_values = [False,True,True,True,True,True,True,True,True,True]
    for i in range(len(available_values)):
        if available_values[i]:
            available_values[i] = check_row(sqr_coord, board, i)
        if available_values[i]:
            available_values[i] = check_column(sqr_coord, board, i)
        if available_values[i]:
            available_values[i] = check_box(sqr_coord, board, i)
    print ("The available numbers are:")
    print ([i for i, x in enumerate(available_values) if x])

def check_box(sqr_coord,board,value):
    is_in_box = True
    row = (sqr_coord[0] // 3) *3
    column = (sqr_coord[1] // 3) * 3
    for r in range(row,row+3):
        for c in range(column, column+3):
            if board[r][c] == value:
                is_in_box = False
    return is_in_box

def check_column(sqr_coord,board,value):
    is_in_column = True
    for i in range(9):
        if value == board[i][sqr_coord[1]]:
            is_in_column = False
    return is_in_column

def check_row(sqr_coord,board,value):
    is_in_row = True
    if value in board[sqr_coord[0]]:
        is_in_row = False
    return is_in_row

def play_game(board):
    continue_playing = True

    while continue_playing:
        user_square = get_user_square()

        if user_square[0] == "s":
            file_name = input ("What do you want to save the board as?")
            save_board(file_name,board)
            continue_playing = False
            break
        
        user_input_value = get_input_value()
        if user_input_value.lower() == "s":
            file_name = input ("What do you want to save the board as?")
            save_board(file_name,board)
            continue_playing = False
        elif user_input_value.lower() == "q":
            show_available_values(user_square, board)
            display_board(board)
        elif(continue_playing == True):
            board = update_board(board,user_square,user_input_value)
            display_board(board)
        


def main():
    board = read_board()

    display_board(board)

    play_game(board)


if __name__ == "__main__":
    main()