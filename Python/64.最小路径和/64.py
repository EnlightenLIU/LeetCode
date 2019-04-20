'''
@Author: 拎把木剑当大侠
@Description: 
@Date: 2019-04-20 18:37:41
@LastEditTime: 2019-04-20 18:56:57
'''


class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or len(grid) == 0:
            return 0

        row = len(grid)
        if row:
            col = len(grid[0])
        else:
            col = 0

        for i in range(1, col):
            grid[0][i] += grid[0][i-1]
        for j in range(1, row):
            grid[j][0] += grid[j-1][0]
        for i in range(1, row):
            for j in range(1, col):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[-1][-1]
