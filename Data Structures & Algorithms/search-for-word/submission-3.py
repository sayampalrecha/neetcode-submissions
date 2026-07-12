class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        length = len(word)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # prune1
        count_board = Counter(c for row in board for c in row)
        count_word = Counter(word)
        for char in count_word:
            if count_board[char] < count_word[char]:
                return False
        
        # prune2
        if count_board[word[0]] > count_board[word[-1]]:
            word = word[::-1]

        def bfs(x, y, i):
            if i == length:
                return True

            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != word[i]:
                return False
            
            origin = board[x][y]
            board[x][y] = None
            for dx, dy in directions:
                cx, cy = x+dx, y+dy
                if bfs(cx, cy, i+1):
                    return True
            board[x][y] = origin
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bfs(i, j, 0):
                        return True
        return False