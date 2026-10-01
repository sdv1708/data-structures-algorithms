class Solution:
    def reorganizeString(self, s: str) -> str:
        N = len(s)
        freq = Counter(s)
        if max(freq.values()) > (N + 1) // 2: 
            return "" 
 
        maxHeap = []
        result = []
        prev = None 

        for char, count in freq.items():
            heapq.heappush(maxHeap, (-count, char)) 

        
        
        while maxHeap:
            f, c = heapq.heappop(maxHeap) 
            result.append(c)
            f += 1

            if prev: 
                heapq.heappush(maxHeap, prev)
                prev = None 
            
            if f < 0: 
                prev = (f, c)

            
        return "".join(result)




        


        