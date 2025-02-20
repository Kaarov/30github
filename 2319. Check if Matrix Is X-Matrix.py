from typing import List


class Solution:
    def checkXMatrix(self, grid: List[List[int]]) -> bool:
        length = len(grid)
        for i in range(length):
            for j in range(length):
                if i == j or i + j == length - 1:
                    if grid[i][j] == 0:
                        return False
                else:
                    if grid[i][j] != 0:
                        return False
        return True
