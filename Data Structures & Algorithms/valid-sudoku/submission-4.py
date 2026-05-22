class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row
        for i in range(9):
            row = []
            for j in range(9):
                if board[i][j]!= ".":
                    if board[i][j] in row:
                        return False
                    row.append(board[i][j]) 
        #for column    
        for i in range(9):
            column = []
            for j in range(9):
                if board[j][i] != ".":
                    if board[j][i] in column:
                        return False
                    column.append(board[j][i])
        
        #for square
        for square in range(9):
            box = []
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    column = (square % 3) * 3 + j
                    if board[row][column] != ".":
                        if board[row][column] in box:
                            return False
                        box.append(board[row][column])



        return True
    