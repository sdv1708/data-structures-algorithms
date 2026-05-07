class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: 
            freq[num] = 1 + freq.get(num, 0) 
        
        minHeap = []

        for num, f in freq.items(): 
            heapq.heappush(minHeap, (f, num))
            if len(minHeap) > k: 
                heapq.heappop(minHeap)
        
        return [num for f, num in minHeap]
        