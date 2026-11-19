import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:



        # A,A,A,B,C. n = 3
        # A,B,C, idle, A,idle, idle, idle, A

        # at t = 0,
        # Assign CPU to tasks that have the highest freq
        # Put them in cooldown until t + n

        # Max heap

        task_freq = {}
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        max_heap = [(-freq, task) for task, freq in task_freq.items()]
        heapq.heapify(max_heap)

        time = 0
        q = deque()

        while max_heap or q:
            time += 1
            if max_heap:
                freq, task = heapq.heappop(max_heap)
                freq += 1
                time_cooled_for = time + n
                if freq:
                    q.append([freq, task, time_cooled_for])
            else:
                time = q[0][2]
            if q and q[0][2] == time:
                freq, task, time_cooled_for = q.popleft()
                heapq.heappush(max_heap, (freq, task))

        return time
    
        
        