from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Convert each column into a set and check len == 9
        for idx in range(len(board)):
            column = [row[idx] for row in board]
            if self.has_duplicates(column):
                return False

        # Convert each row into a set and check len == 9
        for idx in range(len(board)):
            if self.has_duplicates(board[idx]):
                return False

        for offsetx in range(0,3):
            for offsety in range(0,3):
                if self.squareHasDuplicate(board,offsetx,offsety):
                    return False

        return True
    

    
    def has_duplicates(self,row, ignore_char='.'):
        seen = set()
        for char in row:
            if char != ignore_char:
                if char in seen:
                    return True  # Found a duplicate
                seen.add(char)
        return False  # No duplicates
    
    # offsetx = 0, offsety=0
    # 1,2,.
    # 4,.,.
    # .,9,8
    def squareHasDuplicate(self,board,offsetx,offsety,ignore_char='.'):
        seen = set()
        for row in range(offsetx*3,(offsetx*3)+3):
            for column in range(offsety*3,(offsety*3)+3):
                if board[row][column] in seen and board[row][column]!=ignore_char:
                    return True
                else:
                    seen.add(board[row][column])
        return False

        

        
        # Convert each square into a set and check len == 9
            # what is a square, it's a 3*3 box which means there's
            # 9 total in a 9*9 grid
    
board=[
    ["1","2",".",".","3",".",".",".","."],
    ["4",".",".","5",".",".",".",".","."],
    [".","9","8",".",".",".",".",".","3"],
    ["5",".",".",".","6",".",".",".","4"],
    [".",".",".","8",".","3",".",".","5"],
    ["7",".",".",".","2",".",".",".","6"],
    [".",".",".",".",".",".","2",".","."],
    [".",".",".","4","1","9",".",".","8"],
    [".",".",".",".","8",".",".","7","9"]
    ]

Solution().isValidSudoku(board)