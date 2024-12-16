import matplotlib.pyplot as plt
import networkx as nx


def visualize_park_graph(G):
    """
    Visualize the park graph with node positions and edges.

    Node color will represent the probability of finding the lost object.
    Edge widths or colors can represent the weight (distance).
    """

    # Create a figure and an axes object explicitly
    fig, ax = plt.subplots(figsize=(8, 6))

    # Extract node positions
    pos = nx.get_node_attributes(G, 'pos')

    # Extract node probabilities for color mapping
    probabilities = nx.get_node_attributes(G, 'probability')
    # Create a list of probabilities in node order
    probs_list = [probabilities[n] for n in G.nodes()]

    # Set up a color map for probabilities
    cmap = plt.cm.viridis
    node_colors = [cmap(p / max(probs_list)) for p in probs_list]

    # Draw the nodes on the specified axes
    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=300, edgecolors='black', ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=8, font_color='white', ax=ax)

    # Draw edges with weights
    edges = G.edges(data=True)
    weights = [e[2]['weight'] for e in edges]

    # Normalize edge widths for better visuals
    max_w = max(weights) if weights else 1
    widths = [2.0 * (w / max_w) for w in weights]

    nx.draw_networkx_edges(G, pos, width=widths, alpha=0.7, ax=ax)

    # Create a colorbar for probabilities
    sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(probs_list), vmax=max(probs_list)))
    sm.set_array([])

    # Pass the axes to plt.colorbar so it knows where to place it
    cbar = plt.colorbar(sm, ax=ax)
    cbar.set_label('Probability of Lost Object')

    ax.set_title("Park Graph Visualization")
    ax.axis('off')
    plt.tight_layout()
    plt.show()
