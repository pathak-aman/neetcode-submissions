from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Question is asking for first true
        
        # Range: [1, max(piles)]
        # Brute Force: O(max(piles)) * N
        # Impossible case: hours < len(piles)

        # Handlede by constraints: 
        if h < len(piles):
            return -1

        def can_eat(piles, h, k):
            print(k)
            time = 0
            for pile in piles:
                time += ceil(pile/k)
            return time <= h

        low = 1
        high = max(piles)

        while low <= high:
            mid = (low + high)//2
            if can_eat(piles, h, mid):
                high = mid -1
            else:
                low = mid + 1
        return low



        # 1,4,3,2, 
        # h = 9
        
        # low = 1
        # high = 4

        # mid = 5//2 = 2

        # can_eat(piles,9,2)
        # time = 1 + 2 + 2 + 1 <= 9
        # high = 1

        # mid = 2//2 = 1
        # can_eat(piles, 9,1)
        # time = 1 + 4 + 3 + 2 !<= 9
        # low = 2.





