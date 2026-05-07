class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
    
        minHeap = []
        
        for num, f in freq.items():
            heapq.heappush(minHeap, (f, num))
            if len(minHeap) > k:
                heapq.heappop(minHeap)
        
        # The heap now contains the K most frequent elements
        return [num for f, num in minHeap]
        

        