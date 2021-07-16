# Dynamic programming solution O(N) in time, O(1) space
def unstableString(s):
	N, output, zeros, ones = len(s), 0, 0, 0
	for i in range (N):
		if s[i] == "0":
			zeros, ones = ones + 1, 0
		elif s[i] == "1":
			zeros, ones = 0, zeros + 1
		else:
			zeros, ones = ones + 1, zeros + 1
		output += max(zeros, ones)
	return output

# Driver code
t = int(input())
for i in range (t):
	s = input()
	print(unstableString(s))
