class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        N =len(matrix)
        M = len(matrix[0])

        rowMin = []
        for i in range(N):
            rMin = float('inf')
            for j in range(M):
                rMin = min(rMin,matrix[i][j])
            rowMin.append(rMin)
        
        colMax = []
        for j in range(M):
            cMax = float('-inf')
            for i in range(N):
                cMax = max(cMax,matrix[i][j])
            colMax.append(cMax)
        
        luckyNumbers = []
        for i in range(N):
            for j in range(M):
                if matrix[i][j] == rowMin[i] and matrix[i][j] == colMax[j]:
                    luckyNumbers.append(matrix[i][j])
                
        return luckyNumbers


       
        return []

        
