class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            li = matrix[i][-1]
            if target > li:
                continue
            else:
                l = 0
                r = m-1
                while l<= r:
                    mid = l+(r-l)//2
                    if matrix[i][mid] == target:
                        return True
                    elif matrix[i][mid] < target:
                        l = mid + 1
                    else:
                        r = mid - 1

        return False

        