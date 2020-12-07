from dfs import depth_first_search, depth_first_search_recursive
from bfs import breadth_first_search
from top_sort import topological_sort
from dijkstra import find_shortest_path
from bellman_ford import bellman_ford_distance

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

    # print(depth_first_search(graph, "A", "G"))
    # print(depth_first_search_recursive(graph, "A", "G", set()))

    # print(breadth_first_search(graph, "A", "G"))

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

    # print(topological_sort(graph))  # ['E', 'F', 'K', 'C', 'B', 'A', 'D', 'H', 'J', 'M', 'G', 'I', 'L']

    graph = {
        "A": [("B", 5), ("C", 1)],
        "B": [("C", 2), ("D", 3), ("E", 20)],
        "C": [("B", 3), ("E", 12)],
        "D": [("C", 3), ("E", 2), ("F", 6)],
        "E": [("F", 1)],
        "F": [],
    }

    print(find_shortest_path(graph, "A", "F"))


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

    print(bellman_ford_distance(graph, "A"))
