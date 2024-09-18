
import sys
from heapq import heappush, heappop

def dijkstra(graph, source):
    # Determine the maximum node index
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors.keys())
    max_node = max(nodes, default=-1)

    # Initialize distances and paths
    dist = [sys.maxsize] * (max_node + 1)
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {i: [] for i in range(max_node + 1)}
    
    while heap:
        w, u = heappop(heap)
        
        if dist[u] < w:
            continue
        
        for v in graph.get(u, {}):
            new_dist = w + graph[u][v]
            if new_dist < dist[v]:
                dist[v] = new_dist
                path[v] = path[u] + [u]
                heappush(heap, (new_dist, v))
    
    # Debugging output
    print('Final distances:', dist)
    print('Final paths:', path)
    
    return dist, path


