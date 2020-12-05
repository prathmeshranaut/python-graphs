def depth_first_search(graph: dict, start: str, search: str) -> bool:
    stack = [start]
    visited = set()

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node == search:
            return True

        if current_node not in visited and len(graph[current_node]) > 0:
            list = graph[current_node][::-1]
            for element in list:
                if element not in visited:
                    stack.append(element)

        visited.add(current_node)
        print(stack)

    return False


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
