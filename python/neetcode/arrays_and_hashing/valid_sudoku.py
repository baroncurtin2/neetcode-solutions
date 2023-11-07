def is_valid_sudoku(board: list[list[str]]) -> bool:
    """Determines if the board is a valid sudoku

    Args:
        board (list[list[str]]): sudoku board with some elements populated

    Returns:
        bool: True if valid, else False
    """
    result = set()

    for i, row in enumerate(board):
        for j, ele in enumerate(row):
            if ele == ".":
                continue

            row_key = (i, ele)
            col_key = (ele, j)
            sq_key = (i // 3, j // 3, ele)

            if check_unique(row_key, col_key, sq_key, result):
                return False

            result.add((i, ele))
            result.add((ele, j))
            result.add((i // 3, j // 3, ele))

    return True


def check_unique(
    row_key: tuple, col_key: tuple, sq_key: tuple, result_set: set
) -> bool:
    keys = [row_key, col_key, sq_key]
    return any((key in result_set for key in keys))
