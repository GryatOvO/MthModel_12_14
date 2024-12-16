import matplotlib.pyplot as plt
import networkx as nx


def visualize_park_graph_no_prob(G):
    """
    Visualize the park graph with node positions and edges.

    Node color will represent the probability of finding the lost object.
    Edge widths or colors can represent the weight (distance).
    """

    # Create a figure and an axes object explicitly
    fig, ax = plt.subplots(figsize=(8, 6))

    # Extract node positions
    pos = nx.get_node_attributes(G, 'pos')


    # Draw the nodes on the specified axes
    nx.draw_networkx_nodes(G, pos, node_size=300, edgecolors='black', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='white', ax=ax)

    # Draw edges with weights
    edges = G.edges(data=True)
    weights = [e[2]['weight'] for e in edges]

    # Normalize edge widths for better visuals
    max_w = max(weights) if weights else 1
    widths = [2.0 * (w / max_w) for w in weights]

    nx.draw_networkx_edges(G, pos, width=widths, alpha=0.7, ax=ax)

    # Pass the axes to plt.colorbar so it knows where to place it

    ax.set_title("Park Graph Visualization")
    ax.axis('off')
    plt.tight_layout()
    plt.show()
