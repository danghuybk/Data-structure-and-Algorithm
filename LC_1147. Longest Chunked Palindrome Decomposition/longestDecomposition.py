class StringHashing:

	def __init__(self, N, s):
		self.BASE, self.MOD = 911382323, 972663749
		self.hash_table, self.pol = [0] * N, [1] * N
		
		self.hash_table[0] = ord(s[0])
		for i in range (1, N):
			self.hash_table[i] = (self.hash_table[i - 1] * self.BASE + ord(s[i])) % self.MOD
			self.pol[i] = (self.pol[i - 1] * self.BASE) % self.MOD

	def get_hash(self, start, end):
		if start == 0:
			return self.hash_table[end]
		else:
			return (self.hash_table[end] - self.hash_table[start - 1] * self.pol[end - start + 1]) % self.MOD


class Solution:
  
    def longestDecomposition(self, text: str) -> int:
        N = len(text)
        SH, dp = StringHashing(N, text), [-1] * (N + 1)
        
        dp[0] = 0
        for i in range (1, N + 1):
            for j in range (0, i):
                if dp[j] != -1 and SH.get_hash(j, i - 1) == SH.get_hash(N - i, N - j - 1):
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return dp[-1]
