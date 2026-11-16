class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0

        visited = [[0 for _ in range(m)] for _ in range(n)]

        delta_x = [1,0,-1,0]
        delta_y = [0,-1,0,1]

        def dfs(x,y):
            if x < 0 or x==n or y < 0 or y==m:
                return 0
            if not grid[x][y] or visited[x][y]:
                return 0

            visited[x][y] = 1

            right = dfs(x + delta_x[0],y + delta_y[0])
            down = dfs(x + delta_x[1],y + delta_y[1])
            left = dfs(x + delta_x[2],y + delta_y[2])
            up = dfs(x + delta_x[3],y + delta_y[3])
              
            return 1 + right + down + up + left


        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    area = dfs(i,j)
                    max_area = max(max_area, area)

        return max_area