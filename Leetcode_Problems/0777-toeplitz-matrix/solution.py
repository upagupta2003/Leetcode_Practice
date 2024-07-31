class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        # groups = {}
        # for r, row in enumerate(matrix):
        #     for c, val in enumerate(row):
        #         if r-c not in groups:
        #             groups[r-c] = val
        #             print(groups)
        #         elif groups[r-c] != val:
        #             return False
        # return True
          
        R = len(matrix)
        C = len(matrix[0])

        for c in range(0,C):
            start = matrix[0][c]

            for k in range(min(R,C-c)):
                if matrix[k][c+k] != start:
                    return False
        
        for r in range(R):
            start = matrix[r][0]
            for k in range(min(R-r,C)):
                if matrix[r+k][k] != start:
                    return False
        return True
        
