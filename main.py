from dfs import depth_first_search, depth_first_search_recursive

def print_hi(name):
    print(f'Hi, {name}')


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

    #print(depth_first_search(graph, "A", "G"))
    print(depth_first_search_recursive(graph, "A", "G", set()))


