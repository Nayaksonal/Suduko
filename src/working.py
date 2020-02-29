import argparse
import copy

# board = [
#     # [7, 0, 9, 0, 0, 2, 6, 8, 0],
#     # [0, 0, 2, 0, 5, 0, 7, 0, 4],
#     # [0, 0, 0, 0, 0, 0, 2, 0, 0],
#     # [1, 9, 0, 0, 0, 7, 0, 6, 0],
#     # [8, 6, 7, 1, 9, 5, 0, 4, 0],
#     # [5, 0, 4, 0, 0, 0, 0, 9, 0],
#     # [4, 3, 5, 7, 8, 0, 0, 2, 0],
#     # [0, 0, 6, 4, 0, 0, 0, 0, 1],
#     # [9, 8, 0, 5, 0, 6, 0, 0, 3]
# ]

# board = []

emptycell_pos = []
empty_cells_proposed_values = {}


def print_board(board):
    print('\n')
    for i in range(9):
        print(f"{board[i]}\n")


def get_previous_cell_position(row, col):

    for i, j in enumerate(emptycell_pos):
        if ((row, col)) == j:
            if i > 0:
                return emptycell_pos[i-1][0], emptycell_pos[i-1][1]
    return None, None


def suduko_entry(board_input):

    global board
    board = copy.deepcopy(board_input)
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                empty_cells_proposed_values[(i, j)] = []
                if (i, j) in emptycell_pos:
                    pass
                else:
                    emptycell_pos.append((i, j))
                found_status = find_number_wrapper(i, j, 'forward')

    if check_suduko_resolved_status(board):
        print('solved suduko :\n')
        print_board(board)
    else:
        print_board(board)
        print('Suduko puzzle is unresolved')


def check_suduko_resolved_status(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return False

    return True


def find_number_wrapper(row, col, rule):
    if row > 8 or col > 8:
        return False
    old_value = board[row][col]
    # Storing values in dict for backtracking
    if old_value != 0:
        empty_cells_proposed_values[(row, col)].append(old_value)
        board[row][col] = 0

    status = find_number(row, col, rule)
    # Tracking backward
    if not status:
        old_row, old_col = get_previous_cell_position(row, col)
        if old_row is not None or old_col is not None:
            # Calling function recursively for last position
            status_1 = find_number_wrapper(old_row, old_col, rule='backward')
        else:
            return False
        # Calling wrapper for current position
        if status_1:
            _ = find_number_wrapper(row, col, rule='forward')
        else:
            return False
    return True


def find_number(row, col, rule):
    if rule == 'forward':
        barred_numbers = []
        empty_cells_proposed_values[(row, col)] = []
    else:
        barred_numbers = empty_cells_proposed_values[(row, col)]

    for i in range(1, 10):
        # Checking rule , if it is for forward number then checking is for
        if i not in barred_numbers:
            status = validity_checker(board, i, (row, col))
            if status:
                board[row][col] = i
                return True
    return False


def validity_checker(board, num, pos):

    row = pos[0]
    col = pos[1]
    # checking validity of num in row
    status = True
    # print(f'start of row validation: {num}')
    for i in range(9):
        if num == board[row][i]:
            status = False

            return status

    # checking validity of num in _column
    for i in range(9):
        if num == board[i][col]:
            # print(f'position of occurrence col : ({i},{col}) : {board[i][col]}')
            status = False
            # new_pos = (i, col)
            return status

    #check for grid
    if row < 3:
        start_row_pos = 0
    elif row < 6:
        start_row_pos = 3
    else:
        start_row_pos = 6

    if col < 3:
        start_col_pos = 0
    elif col < 6:
        start_col_pos=3
    else:
        start_col_pos=6

    for i in range(start_row_pos, start_row_pos+3):
        for j in range(start_col_pos, start_col_pos+3):
            # print(i,j)
            if num == board[i][j]:
                status = False
                _ = (i, j)
                return status
    return True


def process_args():
    parser = argparse.ArgumentParser(description='Suduko Game')
    parser.add_argument('--board_input', metavar='board_input',
                        nargs='+', type=str,
                        help='Please enter suduko puzzle as array of 81 numbers')
    # known_arg, arg_list = parser.parse_known_args()
    known_arg = parser.parse_args().board_input[0].split(',')
    board = []
    if len(known_arg) < 81:
        print('your list is not complete it needs to have 81 numbers')
        exit(0)

    j = 0
    while j < 81:
        row = []
        for i in range(9):
            row.append(int(known_arg[i+j]))
        j = j + 9
        board.append(row)
    return board


def main():
    board_input = process_args()
    # print_board(board)
    suduko_entry(board_input)


if __name__ == '__main__':
    main()
