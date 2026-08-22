class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def add(i,j):
            if i<0 or j<0 or i>=ROWS or j>=COLS or (i,j) in visit or grid[i][j] == -1:
                return
            q.append([i,j])
            visit.add((i,j))    
              


        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append([i,j])
                    visit.add((i,j))
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.popleft()
                grid[r][c] = dist
                add(r+1,c)
                add(r-1,c)
                add(r,c-1)
                add(r,c+1)
            dist+=1    


             

        