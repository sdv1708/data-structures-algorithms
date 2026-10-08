class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for ind, task in enumerate(tasks): 
            task.append(ind) 
        tasks.sort(key=lambda t : t[0]) 

        result, minHeap = [], []
        ind, time = 0, tasks[0][0] # time starts at the first enqueue time 

        while minHeap or ind < len(tasks): 
            while ind < len(tasks) and time >= tasks[ind][0]:
                heapq.heappush(minHeap, [tasks[ind][1], tasks[ind][2]])
                ind += 1 
            
            if not minHeap: 
                time = tasks[ind][0] 
            else: 
                procTime, index = heapq.heappop(minHeap)
                time += procTime 
                result.append(index)
        
        return result


        
        