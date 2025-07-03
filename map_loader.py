def dummy_neighbors(node):
    """
    Returns neighbors of a node. Extend this for full grid/graph simulation.
    """
    dummy_map = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D'],
        'D': ['E'],
        'E': []
    }
    return dummy_map.get(node, [])
