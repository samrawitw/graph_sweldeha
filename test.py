from graphs_graph_sweldeha import sp
import sys



if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        print(f'Use: {sys.argv[0]} graph_file')
        sys.exit(1)

    graph = {}
    with open(sys.argv[1], 'rt') as f:
        for line in f:
            line = line.strip()
            if line:  # Ensure non-empty line
                s, d, w = line.split()
                s = int(s)
                d = int(d)
                w = int(w)
                if s not in graph:
                    graph[s] = {}
                graph[s][d] = w
    
    # Ensure all nodes are included, even if they have no edges
    all_nodes = set()
    for src, edges in graph.items():
        all_nodes.add(src)
        all_nodes.update(edges.keys())
    for node in all_nodes:
        if node not in graph:
            graph[node] = {}

    print('Graph:', graph)
    
    s = 0
    try:
        dist, path = sp.dijkstra(graph, s)
        print(f'Shortest distances from {s}:')
        print(dist)
        for d in range(len(dist)):
            if dist[d] < sys.maxsize:
                print(f'spf to {d}: {path.get(d, [])}')
            else:
                print(f'spf to {d}: No path')
    except Exception as e:
        print('Error during Dijkstra computation:', e)
