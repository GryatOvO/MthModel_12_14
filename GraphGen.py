import networkx as nx

from mthmodel_12_14.GraphVis import visualize_park_graph

"""
    Generate a random graph representing a park.
        
    Parameters:
    - num_nodes: Number of areas (nodes) in the park
    - area_width, area_height: Dimensions of the park area in meters
    - connection_radius: Maximum distance for which we consider 
                        two points to be connected by a path
        
        Returns:
         A networkx Graph with:
         - node attributes:
            'pos': (x, y) coordinates of the node
            'probability': relative probability of the lost object being here
        - edge attributes:
            'weight': the walking distance between nodes
            """


def generate_park_graph(num_nodes=20, area_width=2000, area_height=2000, connection_radius=800):
    import random
    G = nx.Graph()

    # Create nodes with random positions and probabilities
    for i in range(num_nodes):
        x = random.uniform(0, area_width)
        y = random.uniform(0, area_height)
        probability = random.uniform(0.01, 0.1)
        G.add_node(i, pos=(x, y), probability=probability)

    # Connect nodes if they are within a certain radius
    nodes = list(G.nodes(data=True))
    for i, (u, udata) in enumerate(nodes):
        for j, (v, vdata) in enumerate(nodes):
            if i < j:
                ux, uy = udata['pos']
                vx, vy = vdata['pos']
                dist = ((ux - vx)**2 + (uy - vy)**2)**0.5
                if dist <= connection_radius:
                    G.add_edge(u, v, weight=dist)

    # Ensure connectivity if needed
    if not nx.is_connected(G):
        components = list(nx.connected_components(G))
        while len(components) > 1:
            comp_a = components.pop()
            comp_b = components.pop()
            min_dist = float('inf')
            a_chosen = None
            b_chosen = None
            for na in comp_a:
                for nb in comp_b:
                    ax, ay = G.nodes[na]['pos']
                    bx, by = G.nodes[nb]['pos']
                    d = ((ax - bx)**2 + (ay - by)**2)**0.5
                    if d < min_dist:
                        min_dist = d
                        a_chosen = na
                        b_chosen = nb
            G.add_edge(a_chosen, b_chosen, weight=min_dist)
            components = list(nx.connected_components(G))

    return G

park_graph = generate_park_graph()
visualize_park_graph(park_graph)