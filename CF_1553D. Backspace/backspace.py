def solve(s, t):
	N, M = len(s), len(t)
	s_list, t_list = list(s), list(t)

	while s_list and t_list:
		if s_list[-1] == t_list[-1]:
			s_list.pop()
			t_list.pop()
		else:
			s_list.pop()
			if not s_list:
				break
			else:
				s_list.pop()

	return not t_list

Q = int(input())
for _ in range(Q):
	s = input()
	t = input()
	if solve(s, t): print("YES")
	else: print("NO")
