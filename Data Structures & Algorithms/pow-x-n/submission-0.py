class Solution:
    def myPow(self, x: float, n: int) -> float:

        # Even powers -> multiply x, powers half
        # Odd powers -> multiply x with answer and power -1

        is_neg = False
        if n < 0:
            is_neg = True
            n = abs(n)
        
        ans = 1

        while n > 0:
            print(x,n,ans)
            # Even power
            if n%2 == 0:
                x = x * x
                n = n/2
            else:
                # Odd power
                ans = ans * x
                n = n - 1

        if is_neg:
            return 1.0/ans
        else:
            return ans


