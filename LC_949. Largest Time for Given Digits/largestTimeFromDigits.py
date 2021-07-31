from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        output = -1
        perms = permutations(arr)
        for perm in perms:
            hour = int(str(perm[0]) + str(perm[1]))
            minute = int(str(perm[2]) + str(perm[3]))
            if 0 <= hour <= 23 and 0 <= minute <= 59:
                index = hour * 60 + minute
                output = max(output, index)

        if output == -1:
            return ""
        hour = str(output // 60) if len(str(output // 60)) == 2 else "0" + str(output // 60)
        minute = str(output % 60) if len(str(output % 60)) == 2 else "0" + str(output % 60)
        
        return hour + ":" + minute
