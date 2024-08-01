class Solution:

    def find_max(self, grid, i, j):
        max_element = 0
        for r in range(i, i + 3):
            for c in range(j, j + 3):
                max_element = max(max_element, grid[r][c])
        return max_element

    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                maxLocal[i][j] = self.find_max(grid, i, j)
        return maxLocal

