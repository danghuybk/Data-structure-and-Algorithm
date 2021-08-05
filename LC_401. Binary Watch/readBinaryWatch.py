class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        
        def gen_combinations(path, start_idx, one_count):
            if one_count == turnedOn:
                combinations.add(path)
                return
                
            for i in range (start_idx, FULL_SIZE):
                gen_combinations(path | (1 << i), i + 1, one_count + 1)
        
        def bitmaskToHour(bitmask):
            output, hour, minute = 0, 0, 0
            for i in range (FULL_SIZE):
                if bitmask & (1 << i):
                    if i < 6:
                        minute += 1 << i
                    else:
                        hour += 1 << (i - 6)
            if hour > 11 or minute > 59: 
                return ""
            return str(hour) + ":" + str(minute) if minute >= 10 else str(hour) + ":0" + str(minute)
        
        output, combinations, FULL_SIZE = [], set(), 10
        gen_combinations(0, 0, 0)
                
        for combination in combinations:
            hour = bitmaskToHour(combination)
            if hour:
                output.append(hour)
                
        return output
