class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        neigh = {i:[] for i in range(n)}

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    neigh[i].append(j)

        numProvince = 0
        visited= set()

        def bfs(city):
            visited.add(city)
            q = deque()
            q.append(city)
            
            while q:
                c = q.popleft()
                for i in neigh[c]:
                    if i not in visited:
                        q.append(i)
                        visited.add(i)
                
        for i in range(n):
            if i not in visited:
                bfs(i)
                numProvince += 1
        
        return numProvince


