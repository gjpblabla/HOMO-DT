class Solution:
    def solveNQueens(self, n: int) -> list[list[str]]:
        queen = [0] * n
        col = [False] * n
        dig1 = [False] * (2*n-1)
        dig2 = [False] * (2*n-1)
        ans = []
        def dfs(r):
            if r==n:
                ans.append(['.' * c + 'Q' + (n-1-c) * '.' for c in queen])
                return 
            for c, yes in enumerate(col):
                if not yes and not dig1[r+c] and not dig2[r-c]:
                    queen[r] = c
                    col[c] = dig1[r-c] = dig2[r+c] = True
                    dfs(r+1)
                    col[c] = dig1[r-c] = dig2[r+c] = False
        dfs(0)
        return ans
