class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 3*4 = 12 lang
        # vi vil gerne finde mid = low + (high - low)/2
        # første mid:
        # mid = 1 + (12-1)/2 = 5.5 (rounded down) = 5
        # low = matrix[1][1] (1*1) = 1
        # high = matrix[3][4] (3*4) = 12
        # mid = 5
        # so mid is 5//4
        low, high = 0, len(matrix)*len(matrix[0])-1
        rows = len(matrix)
        cols = len(matrix[0])

        while low <= high:
            mid = low+(high-low)//2
            mr, mc = mid//cols, mid%cols
            midval = matrix[mr][mc]
            if midval == target:
                return True
            elif target > midval:
                low = mid+1
            else:
                high = mid-1
            print(midval)
        return False
