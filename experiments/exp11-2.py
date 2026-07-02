import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
nodes = ['E', 'D', 'A', 'F', 'C', 'B', 'H', 'G', 'I']
edges = [
    ('E', 'D'), ('E', 'A'), ('D', 'A'), ('D', 'F'), ('D', 'C'),
    ('A', 'F'), ('A', 'B'), ('F', 'C'), ('F', 'B'), ('C', 'B'),
    ('C', 'H'), ('C', 'G'), ('B', 'H'), ('B', 'G'),
    ('H', 'G'), ('H', 'I'), ('G', 'I')
]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
coloring = {}
available_colors = [0, 1, 2, 3]
saturation = {node: 0 for node in G.nodes()}
degrees = dict(G.degree())
def get_neighbor_colors(node):
    colors = set()
    for neighbor in G.neighbors(node):
        if neighbor in coloring:
            colors.add(coloring[neighbor])
    return colors
while len(coloring) < len(G.nodes()):
    uncolored_nodes = [n for n in G.nodes() if n not in coloring]
    selected_node = max(
        uncolored_nodes,
        key=lambda n: (saturation[n], degrees[n])
    )
    neighbor_colors = get_neighbor_colors(selected_node)
    for color in available_colors:
        if color not in neighbor_colors:
            coloring[selected_node] = color
            break
    for neighbor in G.neighbors(selected_node):
        if neighbor not in coloring:
            neighbor_used_colors = get_neighbor_colors(neighbor)
            saturation[neighbor] = len(neighbor_used_colors)
color_names = {
    0: "Red",
    1: "Green",
    2: "Blue",
    3: "Yellow"
}
custom_palette = {
    0: (1.0, 0.0, 0.0),     
    1: (0.0, 1.0, 0.0),     
    2: (0.0, 0.0, 1.0),     
    3: (1.0, 1.0, 0.0)     
}
node_colors = [custom_palette[coloring[node]] for node in G.nodes()]
chromatic_number = max(coloring.values()) + 1
pos = {
    'E': (0, 0.5),
    'A': (2, 0.8),  'D': (2, 0.2),
    'F': (4, 0.5),
    'B': (6, 0.8),  'C': (6, 0.2),
    'G': (9, 0.8),  'H': (9, 0.2),
    'I': (11, 0.5)
}
plt.figure(figsize=(12, 5))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_color=node_colors,
    node_size=1200,
    font_weight='bold',
    edge_color='black',
    width=1.5
)
plt.title(f"Manual DSATUR Coloring - Chromatic Number = {chromatic_number}")
plt.show()
print("Node Coloring Assignments:")
for node in coloring:
    print(f"{node} -> {color_names[coloring[node]]}")
print("\nChromatic Number =", chromatic_number)