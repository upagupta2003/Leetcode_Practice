class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        c = 0
        rc = defaultdict(int)
        for row in grid:
            rc[tuple(row)] += 1

        for col in zip(*grid):
            if tuple(col) in rc:
                c += rc[tuple(col)]
        return c
                              

