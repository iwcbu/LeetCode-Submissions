class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            """returns total area of the island"""
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == 0:
                return 0
            
            grid[x][y] = 0
            return (1
                    + dfs(x+1, y)
                    + dfs(x, y+1)
                    + dfs(x-1, y)
                    + dfs(x, y-1))

        best = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    best = max(best, dfs(i, j))
        
        return best
                    

                

