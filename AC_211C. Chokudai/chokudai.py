from collections import defaultdict
def solve(S):
	MOD, chokudai = 10 ** 9 + 7, list("chokudai")
	prev = {}
	for i in range(1, len(chokudai)):
		prev[chokudai[i]] = chokudai[i - 1]
	
	freq = defaultdict(int)
	for char in S:
		if char == "c":
			freq[char] += 1
		elif char in chokudai:
			freq[char] +=  + freq[prev[char]]
	return freq["i"] % MOD

S = input
output = solve(S)
print(output)
