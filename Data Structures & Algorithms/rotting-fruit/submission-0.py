from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh_o = 0
        q = deque()
        # Stores the input (i,j)

        # r,d,l,u
        delta_x = [+1, 0, -1, 0]
        delta_y = [0, -1, 0, 1]

        visited = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fresh_o += 1
                elif grid[i][j] == 2:
                    q.append((i,j))
                    visited[i][j] = 1

        time = 0
        while q:
            for _ in range(len(q)):
                x,y = q.popleft()
                for dx,dy in zip(delta_x, delta_y):
                    x_new = x + dx
                    y_new = y + dy

                    if (
                        0 <= x_new < n and
                        0 <= y_new < m and
                        not visited[x_new][y_new] and
                        grid[x_new][y_new] == 1
                    ):
                        fresh_o -= 1
                        q.append((x_new,y_new))
                        visited[x_new][y_new] = 1
            if q:
                time += 1

        if fresh_o:
            return -1
        else:
            return time