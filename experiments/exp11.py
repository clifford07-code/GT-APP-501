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
G.add_edges_from(edges)
coloring = nx.greedy_color(G, strategy='DSATUR')
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
plt.title(f"DSATUR Coloring - Chromatic Number = {chromatic_number}")
plt.show()
print("Node Coloring Assignments:")
for node in coloring:
    print(f"{node} -> {color_names[coloring[node]]}")
print("\nChromatic Number =", chromatic_number)