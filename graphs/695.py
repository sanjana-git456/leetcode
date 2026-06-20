grid = [
  ["1","1","0","0"],
  ["1","1","0","0"],
  ["0","0","1","0"],
  ["0","0","0","1"]
]

def dfs(grid,r,c):
    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
        return 0
    if grid[r][c] == '0':
        return 0
    grid[r][c] = '0'
    return 1 + dfs(grid,r-1,c) + dfs(grid,r,c+1) + dfs(grid,r+1,c) + dfs(grid,r,c-1)

def numIsland(grid):
    max_area = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '1':
                area = dfs(grid,r,c)
                max_area = max(max_area,area)
    return max_area

print(numIsland(grid))