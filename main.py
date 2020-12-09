from dfs import depth_first_search, depth_first_search_recursive
from bfs import breadth_first_search
from top_sort import topological_sort
from dijkstra import find_shortest_path
from bellman_ford import bellman_ford_distance
from tarjans_strongly_connected import find_strongly_connected_components

if __name__ == '__main__':

    graph = {
        "A": ["B", "C", "D"],
        "B": ["A", "D", "E"],
        "C": ["A", "F"],
        "D": ["B", "D"],
        "E": ["B", "F"],
        "F": ["C", "E", "G"],
        "G": ["F"],
    }

    # Perform Depth-First Search using stacks
    print("DFS: ", depth_first_search(graph, "A", "G"))

    # Perform Depth-First Search using recursive function
    print("DFS(Recursive):", depth_first_search_recursive(graph, "A", "G", set()))

    # Perform Breadth-First Search to find a path between A to G
    print("BFS:", breadth_first_search(graph, "A", "G"))

    graph = {
        "A": ["D"],
        "B": ["D"],
        "C": ["A", "B"],
        "D": ["G", "H"],
        "E": ["A", "D", "F"],
        "F": ["K", "J"],
        "G": ["I"],
        "H": ["I", "J"],
        "I": ["L"],
        "J": ["M", "L"],
        "K": ["J"],
        "L": [],
        "M": [],
    }

    # Finds the Topological order of nodes in the graph
    print("Topological Order:", topological_sort(graph))
    # Expected Output = ['E', 'F', 'K', 'C', 'B', 'A', 'D', 'H', 'J', 'M', 'G', 'I', 'L']

    graph = {
        "A": [("B", 5), ("C", 1)],
        "B": [("C", 2), ("D", 3), ("E", 20)],
        "C": [("B", 3), ("E", 12)],
        "D": [("C", 3), ("E", 2), ("F", 6)],
        "E": [("F", 1)],
        "F": [],
    }

    # Use Djikstra to find shortest path between two nodes in a graph with no negative weights
    print("Shortest Path from A to F:", find_shortest_path(graph, "A", "F"))

    graph = {
        "A": [("B", 5)],
        "B": [("C", 20), ("G", 60), ("F", 30)],
        "C": [("D", 10), ("E", 75)],
        "D": [("C", -15)],
        "E": [("J", 100)],
        "F": [("G", 5), ("E", 25), ("I", 50)],
        "G": [("H", -50)],
        "H": [("I", -10)],
        "I": [],
        "J": []
    }

    # Finds the distance to all nodes from a single source in a graph with negative weights
    print("Distance from A to every node in graph:", bellman_ford_distance(graph, "A"))

    graph = {
        "A": ["B"],
        "B": ["C"],
        "C": ["A"],
        "D": ["E", "H"],
        "E": ["F"],
        "F": ["G", "A"],
        "G": ["E", "A", "C"],
        "H": ["D", "F"],
    }

    # Finds the strongly connected components in the graph
    connected_components = find_strongly_connected_components(graph)
    ssc = {}
    for node, component in connected_components.items():
        if component not in ssc:
            ssc[component] = []

        ssc[component].append(node)

    print("Strongly Connected Components: ", ssc)
