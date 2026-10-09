import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        result = []
        
        # Only add characters with a count greater than 0
        for count, char in ((a, 'a'), (b, 'b'), (c, 'c')):
            if count > 0:
                heapq.heappush(maxHeap, (-count, char))
                
        while maxHeap:
            count, letter = heapq.heappop(maxHeap)
            
            # Check if the last two characters match the current one
            if len(result) >= 2 and result[-1] == result[-2] == letter:
                if not maxHeap:
                    break  # No alternative characters left to use
                
                # Get the second most frequent character
                count2, letter2 = heapq.heappop(maxHeap)
                result.append(letter2)
                
                # Put the original character back
                heapq.heappush(maxHeap, (count, letter))
                
                # Decrement the count (by adding 1 to the negative value)
                count2 += 1
                if count2 < 0:
                    heapq.heappush(maxHeap, (count2, letter2))
            else:
                result.append(letter)
                count += 1
                if count < 0:
                    heapq.heappush(maxHeap, (count, letter))
                    
        return "".join(result)
