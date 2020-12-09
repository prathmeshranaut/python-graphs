on_stack = {}
stack = []
ids = {}
low_link_value = {}
id = 0
ssc_count = 0


def find_strongly_connected_components(graph: dict):
    global ids, low_link_value, on_stack, stack, id, ssc_count
    ids = {x: False for x in graph}
    low_link_value = {x: 99999 for x in graph}
    on_stack = {x: False for x in graph}
    stack = []

    id = 0
    ssc_count = 0

    for node_key in graph.keys():
        if not ids[node_key]:
            dfs(graph, node_key)

    return low_link_value


def dfs(graph: dict, at: str):
    global ids, low_link_value, on_stack, stack, id, ssc_count
    stack.append(at)
    on_stack[at] = True
    id += 1
    low_link_value[at] = id
    ids[at] = id

    for node in graph[at]:
        if not ids[node]:
            dfs(graph, node)
        if on_stack[node]:
            low_link_value[at] = min(low_link_value[at], low_link_value[node])

    if (ids[at] == low_link_value[at]):
        node = stack.pop()
        while node:
            on_stack[node] = False
            low_link_value[node] = ids[at]
            if node == at:
                break
            if len(stack) > 0:
                node = stack.pop()
            else:
                break
        ssc_count += 1
