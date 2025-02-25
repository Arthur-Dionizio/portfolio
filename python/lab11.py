from random import randint

#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 10 for x in range(10)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 10 for i in range(10)]

def print_board(board):
    print("  A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d.%s." % (row_number, ".".join(row)))
        row_number += 1

letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}
#computer create 5 ships
def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0,9), randint(0,9)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"

def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678910":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHIJ":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    create_ships(HIDDEN_BOARD)
    turns = int(input())
    while turns > 0:
        print('Adivinhe a posição de um navio')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("Você já tentou essa posição.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("atingiu o navio X")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("agua")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1     
        if count_hit_ships(GUESS_BOARD) == 5:
            print("Você venceu")
            break
        print("Você tem " + str(turns) + " turnos restantes")
        if turns == 0:
            print("Você está sem turnos restantes")