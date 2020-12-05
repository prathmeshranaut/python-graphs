from dfs import depth_first_search, depth_first_search_recursive
from bfs import breadth_first_search
from top_sort import topological_sort

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

    print(topological_sort(graph))
