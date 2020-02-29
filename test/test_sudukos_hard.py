from src.working import suduko_entry
from src import working


def test_working_hard():
    board = [
        [0, 0, 0, 0, 7, 4, 3, 1, 6],
        [0, 0, 0, 6, 0, 3, 8, 4, 0],
        [0, 0, 0, 0, 0, 8, 5, 0, 0],
        [7, 2, 5, 8, 0, 0, 0, 3, 4],
        [0, 0, 0, 0, 3, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 2, 7, 9, 8],
        [0, 0, 8, 9, 4, 0, 0, 0, 0],
        [0, 4, 0, 0, 8, 5, 9, 0, 0],
        [9, 7, 1, 3, 2, 6, 4, 8, 5]
    ]
    suduko_entry(board)
    assert working.board[7][0] == 3



