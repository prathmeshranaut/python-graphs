def bellman_ford_distance(graph: dict, start: str):
    dist = {x: 99999 for x in graph}
    dist[start] = 0

    for i in range(len(graph)):
        for key in graph.keys():
            for node in graph[key]:
                node_key = node[0]
                node_cost = node[1]

                if dist[node_key] > dist[key] + node_cost:
                    dist[node_key] = dist[key] + node_cost

    # to detect and mark negative cycles
    for i in range(len(graph)):
        for key in graph.keys():
            for node in graph[key]:
                node_key = node[0]
                node_cost = node[1]
                if dist[node_key] > dist[key] + node_cost:
                    dist[node_key] = -99999

    return dist
