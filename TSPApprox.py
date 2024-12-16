import networkx as nx


def approximate_tsp_route(G):
    # Compute MST
    mst = nx.minimum_spanning_tree(G, weight='weight')

    # Double every edge in the MST to make it Eulerian
    # Create a new graph for this doubling
    doubled = nx.MultiGraph()
    for u, v, data in mst.edges(data=True):
        w = data['weight']
        doubled.add_edge(u, v, weight=w)
        doubled.add_edge(u, v, weight=w)  # Add the edge twice

    # Ensure Eulerian property: now all nodes should have even degree in 'doubled'
    # Check Eulerian
    if not nx.is_eulerian(doubled):
        # This should not happen if MST is connected and all edges are doubled.
        raise ValueError("Graph is not Eulerian after doubling edges. Check logic.")

    # Find Eulerian circuit
    # nx.eulerian_circuit returns a list of edges in the Eulerian path
    eulerian_path = list(nx.eulerian_circuit(doubled))
    # eulerian_path is a sequence of edges: (u,v) pairs

    # Shortcut step:
    # The Eulerian path might visit nodes multiple times. We can 'shortcut' by skipping
    # nodes that have been visited before.
    visited = set()
    tsp_path = []
    for (u, v) in eulerian_path:
        # Add 'u' if it's not visited
        if u not in visited:
            visited.add(u)
            tsp_path.append(u)
    # Add the last node if not visited (usually the last one will be the start node)
    if eulerian_path:
        last_node = eulerian_path[-1][1]
        if last_node not in visited:
            tsp_path.append(last_node)

    return tsp_path
