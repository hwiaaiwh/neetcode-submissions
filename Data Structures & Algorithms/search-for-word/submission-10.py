class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        start = word[0]
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == start:
                    if(self.track(board, word[1:], x, y)):
                        return True
        return False
                
    def track(self, board, word, x, y):
        if len(word) == 0:
            print(0)
            return True
        else:
            c = word[0]
        if (x - 1 >= 0 and board[y][x-1] == c):
            board[y][x] = "!"
            if self.track(board, word[1:], x-1, y):
                return True
            else:
                board[y][x] = c
        if (x + 1 < len(board[0]) and board[y][x+1] == c):
            board[y][x] = "!"
            if self.track(board, word[1:], x+1, y):
                return True
            else:
                board[y][x] = c
        if (y - 1 >= 0 and board[y-1][x] == c):
            board[y][x] = "!"
            if self.track(board, word[1:], x, y-1):
                return True
            else:
                board[y][x] = c
        if (y + 1 < len(board) and board[y+1][x] == c):
            board[y][x] = "!"
            if self.track(board, word[1:], x, y+1):
                return True
            else:
                board[y][x] = c
        
        return False
            
        
        