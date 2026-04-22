class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #for row
        for i in range(9):
            row= []
            for j in range(9):
                if board[i][j] != ".":
                    row.append(board[i][j])
            if len(set(row)) != len(row):
                return False
        
        #for column
        for i in range(9):
            column= []
            for j in range(9):
                if board[j][i] != ".":
                    column.append(board[j][i])
            if len(set(column)) != len(column):
                return False
        
        #for boxes 3 X 3
        for square in range(9):
            box = []
            for i in range(3):
                for j in range(3):
                    r = (square//3) * 3 + i
                    c = (square % 3) * 3 + j
                    if board[r][c] != ".":
                        box.append(board[r][c])
            if len(set(box)) != len(box):
                return False
        
        return True


        
