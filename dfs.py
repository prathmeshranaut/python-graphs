def depth_first_search(graph: dict, start: str, search: str) -> bool:
    stack = [start]
    visited = set(start)

    while len(stack) > 0:
        current_node = stack.pop()
        if current_node == search:
            return True

        if current_node not in visited and len(graph[current_node]) > 0:
            list = graph[current_node][::-1]
            stack.extend(list)

        visited.add(current_node)
        print(stack)

    return False
