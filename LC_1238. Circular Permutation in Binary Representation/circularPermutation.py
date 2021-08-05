class Solution:
    def circularPermutation(self, N: int, start: int) -> List[int]:
        
        def helper(num_val, num_idx, path):
            if output:
                return
            
            for i in range(N):
                cand = num_val ^ (1 << i)
                if cand not in seen:
                    path.append(cand)
                    seen.add(cand)
                    
                    if num_idx == 2 ** N - 1:
                        if cand in last:
                            output.append(path[:])
                    else:
                        helper(cand, num_idx + 1, path)
                    
                    path.pop()
                    seen.discard(cand)
                    
        output, seen, last = [], set([start]), set()
        for i in range (N):
            last.add(start ^ (1 << i))
        helper(start, 1, [start])
        return output[0]
