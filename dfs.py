# Performs depth first search to find if a path exists from a staring node to
# a destination node in a graph.
# Returns True, if a path exists
# Returns False if a path does not exist
def depth_first_search(graph: dict, start: str, search: str) -> bool:
    stack = [start]
    visited = set()

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node == search:
            return True

        if current_node in visited:
            return False

        visited.add(current_node)

        for element in graph[current_node]:
            if element not in visited:
                stack.append(element)

    return False


# Recursive approach to find if an element exists in the graph using DFS
def depth_first_search_recursive(graph: dict, start: str, search: str, visited: set) -> bool:
    if start in visited:
        return False

    # print(start)
    if search == start:
        return True

    visited.add(start)

    list = []
    for i in graph[start]:
        list.append(depth_first_search_recursive(graph, i, search, visited))

    if any(list):
        return True

    return False
