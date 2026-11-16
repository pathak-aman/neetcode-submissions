

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = defaultdict(set) #rows[0-8]
        cols = defaultdict(set) #column[0-8]
        squares = defaultdict(set) #square[(0,0),(3,0),(6,0),(0,3)...]

        for i in range(n):
            for j in range(n):
                val = board[i][j]
                if val == ".":
                    continue
                elif (
                    val in rows[i] or
                    val in cols[j] or
                    val in squares[(i//3,j//3)]
                ):
                    return False
                else:
                    rows[i].add(val)
                    cols[j].add(val)
                    squares[(i//3,j//3)].add(val)

        return True


