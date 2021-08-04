# Tricky part: Prove upper bound max_pos
class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        # Initialize data
        queue, max_pos = deque([(0, 0, True)]), max([x] + forbidden) + a + b
        forbidden, seen = set(forbidden), set()
        
        while queue:
            cur_pos, cur_step, can_backward = queue.popleft()
            if cur_pos == x:
                return cur_step
                
            # Process forward element
            fw_pos = cur_pos + a
            if fw_pos <= max_pos and fw_pos not in forbidden and fw_pos not in seen:
                queue.append((fw_pos, cur_step + 1, True))
                seen.add(fw_pos)
                
            # Process backward element
            bw_pos = cur_pos - b
            if bw_pos >= 0 and bw_pos not in forbidden and bw_pos not in seen and can_backward == True:
                queue.append((bw_pos, cur_step + 1, False))
                seen.add(fw_pos)

        return -1
