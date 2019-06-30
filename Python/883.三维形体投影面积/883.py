class Solution(object):
    def projectionArea(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if len(grid)==0:
            return 0
        rows=len(grid)
        cols=len(grid[0])
        sum1=0
        sum2=0
        sum3=0
        for i in range(rows):
            max_row=grid[i][0]
            for j in range(cols):
                if grid[i][j]:
                    sum1+=1
                if grid[i][j]>max_row:
                    max_row=grid[i][j]
            sum2+=max_row

        for j in range(cols):
            max_col=grid[0][j]
            for i in range(rows):
                if grid[i][j]>max_col:
                    max_col=grid[i][j]
            sum3+=max_col
        return sum1+sum2+sum3

grid=[[2]]
s=Solution()
area=s.projectionArea(grid)
print(area)

