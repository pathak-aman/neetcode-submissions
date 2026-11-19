import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        
        for start, (x,y) in enumerate(points):
            d = (x**2 + y**2)**(1/2)
            heapq.heappush(max_heap, (-d, start))

            if len(max_heap) > k:
                heapq.heappop(max_heap)
        ans = []
        for _ in range(len(max_heap)):
            d, index = heapq.heappop(max_heap)
            ans.append(points[index])
        return ans
        
        


