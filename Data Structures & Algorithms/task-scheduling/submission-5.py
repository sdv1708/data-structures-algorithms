class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks) 

        maxHeap = [-i for i in freq.values()]
        heapq.heapify(maxHeap) 

        time = 0 
        queue = deque() 

        while maxHeap or queue: 
            time += 1 

            if maxHeap: 
                count = 1 + heapq.heappop(maxHeap) # reduce the count of operations

                if count:
                    queue.append([count, time + n])

            if queue and queue[0][1] <= time: 
                heapq.heappush(maxHeap, queue.popleft()[0])


        return time 


        