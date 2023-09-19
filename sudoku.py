def sudoku(puzzle):
    def is_valid(num, row, col):
        if num in puzzle[row]:
            return False

        for i in range(9):
            if puzzle[i][col] == num:
                return False

        rowstart = 3 * (row // 3)
        colstart = 3 * (col // 3)

        for r in range(rowstart, rowstart + 3):
            for c in range(colstart, colstart + 3):
                if puzzle[r][c] == num:
                    return False

        return True

    def solve():
        for row in range(9):
            for col in range(9):
                if puzzle[row][col] == 0:
                    for num in range(1, 10):
                        if is_valid(num, row, col):
                            puzzle[row][col] = num
                            if solve():
                                return True
                            puzzle[row][col] = 0
                    return False
        return True

    if solve():
        return puzzle