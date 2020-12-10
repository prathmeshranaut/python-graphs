# Topological sort returns the ordering of nodes in a graph
# This helps in creating a Directed Acyclic Graph
def topological_sort(graph: dict) -> list:
    v = {x: False for x in graph}
    order = [0] * len(v)
    index = len(v) - 1

    for k in v:
        if not v[k]:
            visited = []

            dfs(graph, k, v, visited)
            for node in visited:
                order[index] = node
                index = index - 1

    return order


def dfs(graph: dict, k: str, v: dict, visited: list):
    v[k] = True

    for node in graph[k]:
        if not v[node]:
            dfs(graph, node, v, visited)

    visited.append(k)
