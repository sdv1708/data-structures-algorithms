class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Edge case: If starting position is a deadend, we can't move
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0
            
        queue = deque(['0000'])
        visited = set()
        count = 0
        for dead in deadends:
            visited.add(dead)
            
        visited.add('0000') # Must mark start as visited to avoid cycles

        while queue:
            for _ in range(len(queue)):
                pin = queue.popleft()
                
                # Turn digits up
                for i, dig in enumerate(pin):
                    dig_up = (int(dig) + 1) % 10
                    # FIX: Slice pin to keep all 4 characters intact
                    recon = pin[:i] + str(dig_up) + pin[i+1:]
                    
                    if recon not in visited:
                        visited.add(recon)
                        queue.append(recon) # FIX: Add to queue to explore later
                        if recon == target:
                            return count + 1 # FIX: Return next step count

                # Turn digits down
                for i, dig in enumerate(pin):
                    dig_down = (int(dig) - 1 + 10) % 10 # Changed variable name for clarity
                    # FIX: Slice pin to keep all 4 characters intact
                    recon = pin[:i] + str(dig_down) + pin[i+1:]
                    
                    if recon not in visited:
                        visited.add(recon)
                        queue.append(recon) # FIX: Add to queue to explore later
                        if recon == target:
                            return count + 1 # FIX: Return next step count
                
            count += 1
            
        return -1 # FIX: Return -1 if queue empties and target is never reached
