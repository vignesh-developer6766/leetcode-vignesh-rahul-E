# Last updated: 8/12/2026, 12:22:37 PM
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != 'O':
                return
            board[r][c] = '#'  # mark safe
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # Step 1: Mark border-connected 'O's
        for i in range(m):
            dfs(i, 0)
            dfs(i, n-1)
        for j in range(n):
            dfs(0, j)
            dfs(m-1, j)
        
        # Step 2: Flip surrounded 'O's to 'X'
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        
        # Step 3: Convert safe marks back to 'O'
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'
