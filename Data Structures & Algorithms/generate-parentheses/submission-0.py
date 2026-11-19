class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def build(curr, open_n, close_n): # O(2 ^(2n) * n)
            # Base cass:
            if len(curr) == 2*n:
                ans.append(curr)
                return
            
            if open_n < n:
                curr += "("
                build(curr, open_n+1, close_n)
                curr = curr[:-1]
            
            if close_n < open_n:
                curr += ")"
                build(curr, open_n, close_n+1)
                curr = curr[:-1]


        build("",0,0)
        return ans