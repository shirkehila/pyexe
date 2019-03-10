def check_row(board, row_num):
    """Checks a single row for winner

    Args:
        board: A 3*3 matrix with cells:
            0 - empty
            1 - player 1
            2 - player 2
        row_num: number of row to check

    Returns:
        0 - no winner
        1 - player 1 won
        2 - player 2 won
    """
    if board[row_num][0] == board[row_num][1] == board[row_num][2]:
        return board[row_num][0]
    return 0
