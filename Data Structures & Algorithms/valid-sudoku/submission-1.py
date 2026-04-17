class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_master = {i:[] for i in range(9)}
        column_master = {i:[] for i in range(9)}
        grid_master = {}

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j])
                box = (i//3, j//3)

                if box not in grid_master:
                    grid_master[box] = []

                if(value in row_master[i] or value in column_master[j] or value in grid_master[box]):
                    return False
                row_master[i].append(value)
                column_master[j].append(value)
                grid_master[box].append(value)
        
        return True
        
        