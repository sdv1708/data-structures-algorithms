class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
            
        queue = deque(['0000'])
       
        visited = set(deadends)
        visited.add('0000')
        count = 0
        
        while queue:
            # Track steps level by level
            for _ in range(len(queue)):
                pin = queue.popleft()
                
                # Check for target when popping from the queue
                if pin == target:
                    return count
                
                for i, dig in enumerate(pin):
                    d = int(dig)
                    # Generate both adjusted digits (up and down)
                    for new_dig in [(d + 1) % 10, (d - 1) % 10]:
                        new_pin = pin[:i] + str(new_dig) + pin[i+1:]
                        
                        # Only visit unexplored, non-deadend combinations
                        if new_pin not in visited:
                            visited.add(new_pin)
                            queue.append(new_pin)
    
            count += 1            
        return -1
