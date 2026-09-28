class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        squares = collections.defaultdict(set)
        for row in range(9):
            rowNumbers = set()
            for column in range(9):
                currNum = board[row][column]
                if currNum == '.': continue
                if currNum in rowNumbers or currNum in squares[(row//3, column//3)]:
                    return False
                rowNumbers.add(currNum)
                squares[(row//3, column//3)].add(currNum)
        for column in range(9):
            columnNumbers = set()
            for row in range(9):
                currNum = board[row][column]
                if currNum == '.': continue
                if currNum in columnNumbers:
                    return False
                columnNumbers.add(currNum)
        return True

        