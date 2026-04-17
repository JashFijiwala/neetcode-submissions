class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_master = {i: [] for i in range(9)}
        column_master = {i: [] for i in range(9)}
        grid_master = {str(i): [] for i in range(1, 10)}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j])

                if value in column_master[j] or value in row_master[i]:
                    return False

                column_master[j].append(value)
                row_master[i].append(value)

                if i < 3 and j < 3 and value not in grid_master["1"]:
                    grid_master["1"].append(value)

                elif i < 3 and j >= 3 and j < 6 and value not in grid_master["2"]:
                    grid_master["2"].append(value)

                elif i < 3 and j >= 6 and j < 9 and value not in grid_master["3"]:
                    grid_master["3"].append(value)

                elif i >= 3 and i < 6 and j < 3 and value not in grid_master["4"]:
                    grid_master["4"].append(value)

                elif i >= 3 and i < 6 and j >= 3 and j < 6 and value not in grid_master["5"]:
                    grid_master["5"].append(value)

                elif i >= 3 and i < 6 and j >= 6 and j < 9 and value not in grid_master["6"]:
                    grid_master["6"].append(value)

                elif i >= 6 and i < 9 and j < 3 and value not in grid_master["7"]:
                    grid_master["7"].append(value)

                elif i >= 6 and i < 9 and j >= 3 and j < 6 and value not in grid_master["8"]:
                    grid_master["8"].append(value)

                elif i >= 6 and i < 9 and j >= 6 and j < 9 and value not in grid_master["9"]:
                    grid_master["9"].append(value)

                else:
                    return False

        return True
