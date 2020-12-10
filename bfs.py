# Does a breadth first search to find if a path exists from a starting node
# to another node
# Returns True if path exists
# Returns False if no path exists
def breadth_first_search(graph: dict, start: str, search: str) -> bool:
    queue = [start]
    visited = set()

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node == search:
            return True

        if current_node not in visited:
            for element in graph[current_node]:
                if element not in visited:
                    queue.append(element)

        visited.add(current_node)

    return False
