from collections import defaultdict
def bomber():
	rows, cols = defaultdict(int), defaultdict(int)
	
	for x, y in targets:
		rows[x], cols[y] = rows[x] + 1, cols[y] + 1

	maxTargetPerRows, maxTargetPerCols = max(rows.values()), max(cols.values())

	maxRows = [key for key, value in rows.items() if value == maxTargetPerRows]
	maxCols = [key for key, value in cols.items() if value == maxTargetPerCols]

	for row in maxRows:
		for col in maxCols:
			if (row, col) not in targets:
				return maxTargetPerRows + maxTargetPerCols

	return maxTargetPerRows + maxTargetPerCols - 1

rows, cols, M = map(int, input().split())
targets = set()
for _ in range (M):
	x, y = map(int, input().split())
	targets.add((x - 1, y - 1))

output = bomber()
print(output)
