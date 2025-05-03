class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        n, m = len(grid), len(grid[0])

        def dfs(x, y):
            """returns size of island, but mainly used to remove island from grid."""
            if not (0 <= x < n and 0 <= y < m) or grid[x][y] == "0":
                return 0

            grid[x][y] = "0"
            return (1
                    + dfs(x+1, y)
                    + dfs(x, y+1)
                    + dfs(x-1, y)
                    + dfs(x, y-1))

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        
        return count
                
