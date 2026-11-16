from queue import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        # Taking queue as the weights are 1.
        n = len(grid)
        distance = [[float("inf") for _ in range(n)] for _ in range(n)]
        distance[0][0] = 0

        if n == 1:
            return 1

        # (distance, row, column)
        q = deque()
        q.append([1,0,0])

        delta_x = [1,0,-1]
        delta_y = [-1,0,1]

        while q:
            curr_distance, x, y = q.popleft()
            
            for dx in delta_x:
                for dy in delta_y:
                    x_new, y_new = x + dx, y + dy

                    # condition: valid movement
                    if (0 <= x_new < n and
                        0 <= y_new < n and
                        grid[x_new][y_new] == 0 and
                        distance[x_new][y_new] > curr_distance + 1):

                        if x_new == n-1 and y_new == n-1:
                            return curr_distance + 1

                        distance[x_new][y_new] = curr_distance + 1
                        q.append([distance[x_new][y_new], x_new, y_new])

                        
        return -1