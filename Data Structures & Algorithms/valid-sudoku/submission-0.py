class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            s = set()
            for j in range(len(board[i])):
                if board[i][j] in s:
                    return False
                elif board[i][j] == ".":
                    continue
                else:
                    s.add(board[i][j])

        for i in range(len(board[0])):
            s = set()
            for j in range(len(board)):
                if board[j][i] in s:
                    return False
                elif board[j][i] == ".":
                    continue
                else:
                    s.add(board[j][i])

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                s = set()

                for r in range(3):
                    for c in range(3):
                        if board[r+i][c+j] in s:
                            return False
                        elif board[r+i][c+j] == ".":
                            continue
                        else:
                            s.add(board[r+i][c+j])
        
        return True

            