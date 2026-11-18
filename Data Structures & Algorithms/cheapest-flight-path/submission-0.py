from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        # stops are the most important
        # cheapest flight with > k stops means nothing for us
        # Djikstra's Algo
        # Distance ~ cost
        # Explore the paths where the stops <= k
        # We don't need queue as stops are being added uniformly and makes it easy to track the minimum stop path 
        # (stop, nodes, cost)

        adj_list = defaultdict(list)
        for to, from_, price in flights:
            adj_list[to].append([from_,price])
        
        cost = [float("inf") for _ in range(n)]
        cost[src] = 0

        q = deque()
        q.append([0, src, 0])

        while q:
            stop, node, cost_path = q.popleft()
            if stop > k:
                continue
            for conn, prices in adj_list[node]:
                total_cost = cost_path + prices
                if total_cost < cost[conn] and stop <= k+1:
                    cost[conn] = total_cost
                    q.append([stop+1, conn, total_cost])
        
        if cost[dst] == float("inf"):
            return -1
        else:
            return cost[dst]





