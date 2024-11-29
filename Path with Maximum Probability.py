from collections import deque
from typing import List
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=[[] for _ in range(n)]

        for i, (u,v) in enumerate(edges):
            adj[u].append((v,succProb[i]))
            adj[v].append((u,succProb[i]))
        q=deque([(start_node,1.0)])
        visited=[False]*n
        visited[start_node]=True
        MAX_pro=[0.0]*n
        MAX_pro[start_node]=1.0
        while q:
            node,wt=q.popleft()
            for nei,cost in adj[node]:
                new_prob=cost*wt
                if new_prob > MAX_pro[nei]:
                    MAX_pro[nei]=new_prob
                    visited[nei]=True
                    q.append((nei,new_prob))
        return MAX_pro[end_node]
ob=Solution()
n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2
print(ob.maxProbability(n,edges,succProb,start,end))
