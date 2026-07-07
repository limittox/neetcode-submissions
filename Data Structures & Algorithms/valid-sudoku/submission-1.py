class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        threeByThreeCheck = False
        for i in range(len(board)):
            if self.isValidRow(board, i) == False or self.isValidCol(board, i) == False:
                return False
            for j in range(len(board[i])):
                if i % 3 == 0 and j % 3 == 0 and self.isValidThreeByThree(board, [i,j]) is False:
                    return False
        
        return True
    
    def isValidThreeByThree(self, board: List[List[str]], start: List[int]):
        startRow, startCol = start
        checkNums = set()
        for i in range(startRow, startRow + 3):
            for j in range(startCol, startCol + 3):
                if board[i][j] != ".":
                    num = int(board[i][j])
                    if num in checkNums:
                        return False
                    checkNums.add(num)
        return True
    
    def isValidRow(self, board: List[List[str]], rowNo: int):
        checkNums = set()
        for s in board[rowNo]:
            if s == ".":
                continue
            num = int(s)
            if num in checkNums:
                return False
            checkNums.add(num)
        return True
    
    def isValidCol(self, board: List[List[str]], colNo: int):
        checkNums = set()

        for i in range(9):
            s = board[i][colNo]
            if s == ".":
                continue
            num = int(s)
            if num in checkNums:
                return False
            checkNums.add(num)

        return True