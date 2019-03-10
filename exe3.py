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


def check_col(board, col_num):
    """Checks a single row for winner

    Args:
        board: A 3*3 matrix with cells:
            0 - empty
            1 - player 1
            2 - player 2
        col_num: number of col to check

    Returns:
        0 - no winner
        1 - player 1 won
        2 - player 2 won
    """
    if board[0][col_num] == board[1][col_num] == board[2][col_num]:
        return board[0][col_num]
    return 0


def check_main_diagonal(board):
    """Checks the main diagonal for winner

    Args:
        board: A 3*3 matrix with cells:
            0 - empty
            1 - player 1
            2 - player 2

    Returns:
        0 - no winner
        1 - player 1 won
        2 - player 2 won
    """

    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    return 0


def check_minor_diagonal(board):
    """Checks the minor diagonal for winner

    Args:
        board: A 3*3 matrix with cells:
            0 - empty
            1 - player 1
            2 - player 2

    Returns:
        0 - no winner
        1 - player 1 won
        2 - player 2 won
    """

    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    return 0


def check_board(board):
    """Checks if player 1 won, player 2 won or there is a draw

    Args:
        board: A 3*3 matrix with cells:
            0 - empty
            1 - player 1
            2 - player 2

    Returns:
        0 - no resolution
        1 - player 1 won
        2 - player 2 won
        3 - it's a draw
    """
    # check all rows for winner
    for i in range(3):
        res = check_row(board,i)
        if res != 0:
            return res

    # check all cols for winner
    for i in range(3):
        res = check_col(board,i)
        if res != 0:
            return res

    # check diagonals for winner
    res = check_main_diagonal(board)
    if res != 0:
        return res

    res = check_minor_diagonal(board)
    if res != 0:
        return res

    # check if there are empty cells and thus no resolution yet
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return 0

    # conclude that it's a draw
    return 3
