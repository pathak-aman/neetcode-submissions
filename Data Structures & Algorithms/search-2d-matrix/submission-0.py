class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[1])
        low = 0
        high = m*n -1

        while low <= high:
            mid = (low + high) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        return False

# [[0]]

# m = 3, n = 4, target = 25


# low = 0, high = 11
# mid = 5
# row = 5 // 4 -> 1
# col = 5 % 4 -> 1

# 11 < 25
# low = 6, high = 11
# mid = 8
# row = 8 // 4 -> 2
# col = 8 % 4 -> 0
# 14 < 25

# low = 9, high = 11
# mid = 10
# row = 10 // 4 -> 2
# col = 10% 4 -> 2

# 30 > 25


# low = 9, high = 9
# mid = 9
# row = 2
# col = 1

# 20 > 25

# low = 10, high = 9



