graphs_sweldeha is a Python package for graph algorithms, including Dijkstra's Shortest Path Algorithm. This package provides efficient methods for finding the shortest paths in weighted graphs and can be easily installed and integrated into your Python projects.The package is flexible and allows easy integration into any Python project. Users can input graphs as adjacency lists from text files, making it highly adaptable for various use cases.
To install the graphs_sweldeha package, you can use pip:
pip install graphs-graph-sweldeha==0.0.0

The graph file should contain the edges in the following format:
source_node destination_node weight
0 1 10
0 2 5
1 2 2
1 3 1
2 1 3
2 3 9
3 4 4

Features
Dijkstra's Shortest Path Algorithm: Compute the shortest paths from a source node to all other nodes in a graph.
Flexible Graph Representation: Input graphs as adjacency lists from text files, making it easy to use and integrate into various applications.
Flexible Graph Representation:
The graph input is provided in a simple text file format, where each line represents an edge in the form of source_node destination_node weight. This adjacency list format allows for a straightforward and intuitive representation of complex graphs

Run the script from the command line:
python test.py graph.txt
Example Output is attached in the Readme doc files

Contribution
Contributions to the library are welcome! Please fork the repository and submit pull requests with improvements or additional features. Ensure that any changes 
adhere to the existing code style and include appropriate test cases.

