class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        queue = deque()
        seen = set()
        m = len(grid)
        n = len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i, j) not in seen:
                    queue.append((i, j))
                    seen.add((i, j))
                    while queue:
                        p, q = queue.popleft()
                        for x, y in directions:
                            if 0 <= x + p < m and 0 <= y + q < n and grid[x + p][q + y] == "1" and (
                            x + p, q + y) not in seen:
                                queue.append((x + p, q + y))
                                seen.add((x + p, q + y))
                    count += 1

        return count

