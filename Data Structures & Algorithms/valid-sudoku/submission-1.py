class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # rows
        for x in range(9):
            dupes = set()
            for y in range(9):
                if board[y][x] == ".":
                    continue
                elif board[y][x] in dupes:
                    print(x,y,dupes)
                    print(1)
                    return False
                else:
                    dupes.add(board[y][x])
        
        # cols
        
        for y in range(9):
            dupes = set()
            for x in range(9):
                if board[y][x] == ".":
                    continue
                elif board[y][x] in dupes:
                    print(2)
                    return False
                else:
                    dupes.add(board[y][x])

        # grids
        
        for g in range(9):
            dupes = set()
            for j in range(3):
                y = (g // 3) * 3 + j
                for i in range(3):
                    x = (g % 3) * 3 + i
                    if board[y][x] == ".":
                        continue
                    elif board[y][x] in dupes:
                        print(3)
                        return False
                    else:
                        dupes.add(board[y][x]) 
        

        return True