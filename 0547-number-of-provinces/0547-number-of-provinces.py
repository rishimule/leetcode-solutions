class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        neig = defaultdict(list)

        for r in range(n):
            for c in range(n):
                if isConnected[r][c] == 1:
                    neig[r].append(c)

        visited = set()
        island = 0

        def bfs(i):
            visited.add(i)
            q = deque()
            q.append(i)

            while q:
                i = q.popleft()
                for j in neig[i]:
                    if j not in visited:
                        visited.add(j)
                        q.append(j)

        for i in range(n):
            if i not in visited:
                bfs(i)
                island += 1
        
        return island

        