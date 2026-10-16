class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums: 
            freq[num] = 1 + freq.get(num, 0) 
        
        minHeap = []

        for num, cnt in freq.items(): 
            heapq.heappush(minHeap, (cnt, num))

            if len(minHeap) > k: 
                heapq.heappop(minHeap)
        
        return [num for (cnt, num) in minHeap]