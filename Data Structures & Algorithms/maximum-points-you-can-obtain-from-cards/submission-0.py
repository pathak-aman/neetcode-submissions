class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        l, r = k, n
        maxpoints = 0 

        while l >= 0:
            curr = sum(cardPoints[0:l] + cardPoints[r:n])
            maxpoints = max(maxpoints, curr)
            l -= 1
            r -= 1
        return maxpoints