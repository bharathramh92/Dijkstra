A Dijkstra package to find the shortest path.

Copy the contents of this repository to python package directory.

Usage example:

	from Dijkstra import Dijkstra, Graph

	graph = Graph()
	graph.addEdge("chennai", "bangalore", transit_time=200)
	graph.addEdge("bangalore", "mysore", transit_time=150)

	dijk = Dijkstra()
	traversal_path = dijk.minPath(graph, "mysore", "bangalore", return_list=True) # minPath returns a list of path in order
