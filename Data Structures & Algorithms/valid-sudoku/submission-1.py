class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        columns = len(board[0]) # 9
        rows = len(board)

        row_check: list[int | str] = ["."] * 10
        column_check: list[int | str] = ["."] * 10

        grid_check: list[dict[int, list[int, int]]] = [{}, {}, {}]
        current_grid = 0

        for row_idx, row in enumerate(board):
            for column_idx, current_char in enumerate(row):
                if current_char.isdigit():
                    value = int(current_char)
                    if row_check[value] != value:
                        row_check[value] = value
                    else:
                        print("Duplicates in rows")
                        return False

                # only check in grid if current_char is a digit
                if current_char.isdigit() and current_char in grid_check[current_grid]:
                    print(f"Duplicate value: {current_char} found in grid: {current_grid}")
                    return False
                else:
                    print(f"inserting {current_char} in current_grid: {current_grid}")
                    grid_check[current_grid][current_char] = [row_idx, column_idx]

                if column_idx == 2 or column_idx == 5:
                    print(f"Current col: {column_idx}, changing to grid {current_grid + 1}")
                    current_grid += 1
                elif column_idx == 8:
                    print(f"Row {row_idx} complete, reseting grid to 0")
                    current_grid = 0

            if row_idx == 2 or row_idx == 5:
                grid_check = [{}, {}, {}] # 3 new empty grid dicts for next 3 rows

            row_check = ["."] * 10

        for current_column in range(columns):
            for current_row in range(rows):
                value = board[current_row][current_column]
                if value.isdigit():
                    if column_check[int(value)] != int(value):
                        column_check[int(value)] = int(value)
                    else:
                        print("Duplicate in columns")
                        return False
            column_check = ["."] * 10

        return True
