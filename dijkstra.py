import sys
import heapq


# Dijkstra Algorithm to find the shortest path between two nodes in a graph with no negative weights
def dijkstra(graph: dict, start: str):
    distance = {x: 99999 for x in graph}
    prev = {x: "" for x in graph}
    visited = {x: False for x in graph}
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    distance[start] = 0

    while len(priority_queue):
        dist_index = heapq.heappop(priority_queue)
        cost = dist_index[0]
        key = dist_index[1]
        visited[key] = True

        if distance[key] < cost:
            continue

        for node in graph[key]:
            node_key = node[0]
            node_cost = node[1]

            if visited[node_key]:
                continue

            if distance[node_key] > cost + node_cost:
                prev[node_key] = key
                distance[node_key] = cost + node_cost
                heapq.heappush(priority_queue, (cost + node_cost, node_key))

    return (distance, prev)


# Finds shortest path between two nodes where no negative weights exists
def find_shortest_path(graph: dict, start: str, end: str):
    dist, prev = dijkstra(graph, start)
    path = []
    if dist[end] >= 99999:
        return path

    at = end
    while at != "":
        path.append(at)
        at = prev[at]

    path.reverse()

    return path
