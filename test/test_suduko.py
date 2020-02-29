from src.working import validity_checker, get_previous_cell_position, suduko_entry, print_board, check_suduko_resolved_status

from src import working


def test_validity_checker_row():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 6, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    valid_status = validity_checker(board, 4, (0, 1))
    # assert  1 == 2
    valid_status_false = validity_checker(board, 8, (0, 1))

    assert valid_status is True
    assert valid_status_false is False


def test_validity_checker_col():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 6, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    valid_status = validity_checker(board, 4, (0, 1))
    assert valid_status is True
    # assert new_pos == (0, 0)


def test_validity_checker_col_for_false():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 1, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    valid_status = validity_checker(board, 5, (4, 4))
    assert valid_status is False


def test_validity_checker_for_grid_for_valid_value():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 1, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    valid_status = validity_checker(board, 3, (4, 4))
    assert valid_status is True


def test_validity_checker_grid():
    board = [
        [7, 4, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 6, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    status = validity_checker(board, 5, (7, 2))
    assert 1 == 1
    assert status is False


def test_working_easy():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 6, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    suduko_entry(board)


def test_check_suduko_resolved_status():
    board = [
        [7, 0, 9, 0, 0, 2, 6, 8, 0],
        [0, 0, 2, 0, 5, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0, 2, 0, 0],
        [1, 9, 0, 0, 0, 7, 0, 1, 0],
        [8, 6, 7, 1, 9, 5, 0, 4, 0],
        [5, 0, 4, 0, 0, 0, 0, 9, 0],
        [4, 3, 5, 7, 8, 0, 0, 2, 0],
        [0, 0, 6, 4, 0, 0, 0, 0, 1],
        [9, 8, 0, 5, 0, 6, 0, 0, 3]
    ]
    status = check_suduko_resolved_status(board)
    assert status is False
    # assert status == False




# def test_find_number_wrapper(mocker):
#     ps = mocker.patch('src.working')
#     ps.return_value.backtrack_pos = [(0, 1), (0, 3), (0, 4), (0, 8), (1, 0), (1, 0)]
#

def test_backtrack_index(mocker):
    working.emptycell_pos = [(1, 1), (2, 3)]
    # last_row, last_col = get_last_cell_position(2, 3)
    last_row, last_col =get_previous_cell_position(2, 3)
    assert (last_row, last_col) == (1, 1)


def test_backtrack_index_for_first_element_in_list(mocker):
    working.emptycell_pos = [(1, 1), (2, 3)]
    last_row, last_col = get_previous_cell_position(1, 1)
    print(last_row)
    assert last_row is None



def test_process_arg(mocker):
    input_list = [10, 20, 40]
    ps =mocker.patch('src.working.argparse')
    ps.return_value.ArgumentParser



