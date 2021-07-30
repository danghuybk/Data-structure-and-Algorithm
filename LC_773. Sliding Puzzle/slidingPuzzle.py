class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        queue, visited, target_board = deque(), set(), [[1, 2, 3],[4,5 , 0]]
        dirrs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        for i in range (2):
            for j in range (3):
                if board[i][j] == 0:
                    queue.append((board, i, j, 0))
                    break
                    
        while queue:
            cur_board, cur_x, cur_y, cost = queue.popleft()
            if cur_board == target_board:
                return cost
            
            visited.add(self.encode(cur_board))
            for dirr in dirrs:
                new_board = copy.deepcopy(cur_board)
                new_x, new_y = cur_x + dirr[0], cur_y + dirr[1]
                
                if 0 <= new_x < 2 and 0 <= new_y < 3:
                    new_board[cur_x][cur_y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[cur_x][cur_y]
                    if self.encode(new_board) not in visited:
                        queue.append((new_board, new_x, new_y, cost + 1))
        
        return -1
    
    def encode(self, board):
        hash_value = ""
        for i in range (2):
            for j in range (3):
                hash_value += str(board[i][j])
        return hash_value
