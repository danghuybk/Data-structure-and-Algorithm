class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N, output, word_dict = len(s), [], set(wordDict)
        
        for bitmask in range (1, 2 ** N):
            if bitmask & (1 << 0) == 0:
                continue

            one_idx = [-1]
            for i in range (N - 1, -1, -1):
                if  bitmask & (1 << i):
                    one_idx.append(N - i - 1)
            
            path, is_valid_path = [], True
            for i in range (1, len(one_idx)):
                start, end = one_idx[i - 1] + 1, one_idx[i]
                if s[start:end + 1] in word_dict:
                    path.append(s[start:end + 1])
                else:
                    is_valid_path = False
                    break
                    
            if is_valid_path:
                output.append(" ".join(path))
        
        return output
