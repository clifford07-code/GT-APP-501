import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    (1, 2, 15), (1, 3, 14), (1, 5, 3),
    (3, 5, 9), (3, 6, 8),
    (5, 6, 15),
    (3, 4, 6),
    (4, 2, 2), (4, 7, 3), (4, 8, 9),
    (2, 8, 17),
    (7, 8, 2),
    (6, 7, 8), (6, 4, 9)
]

G.add_weighted_edges_from(edges)

pos = {
    1: (1, 3),
    2: (6, 3),
    3: (3, 1.5),
    4: (6, 1.5),
    5: (0, 0),
    6: (3, 0),
    7: (6, 0),
    8: (8, 1.5)
}

parent = {node: node for node in G.nodes()}
rank = {node: 0 for node in G.nodes()}

def find(u):
    if parent[u] != u:
        parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    ru, rv = find(u), find(v)
    if ru == rv: return False
    if rank[ru] > rank[rv]: parent[rv] = ru
    elif rank[ru] < rank[rv]: parent[ru] = rv
    else:
        parent[rv] = ru
        rank[ru] += 1
    return True

edges_sorted = sorted(edges, key=lambda x: x[2])
steps = []
mst_edges = []
total_cost = 0

for u, v, w in edges_sorted:
    if union(u, v):
        mst_edges.append((u, v, w))
        total_cost += w
        steps.append((list(mst_edges), total_cost))


rows, cols = 2, 4
fig, axes = plt.subplots(rows, cols, figsize=(20, 10))
axes = axes.flatten()

fig.suptitle("Minimum Spanning Tree: Kruskal’s Algorithm ", 
             fontsize=22, fontweight='bold', y=0.98)

def draw_base(ax, title):
    ax.set_title(title, fontsize=14, fontweight='bold', pad=10)
    ax.set_xlim(-1, 10)
    ax.set_ylim(-1, 4)
    ax.axis('off')

ax0 = axes[0]
draw_base(ax0, "Original Graph")
nx.draw(G, pos, with_labels=True, node_color='lightgreen', edgecolors='black', 
        node_size=1000, font_size=10, width=1, edge_color='gray', ax=ax0)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8, ax=ax0)

for i, (edge_list, cost) in enumerate(steps):
    ax = axes[i + 1]
    draw_base(ax, f"Step {i+1} (Total Cost: {cost})")
    

    nx.draw_networkx_nodes(G, pos, node_color='lightgreen', edgecolors='black', 
                           node_size=1000, ax=ax)
    nx.draw_networkx_labels(G, pos, font_size=10, ax=ax)

    if len(edge_list) > 1:
        nx.draw_networkx_edges(G, pos, edgelist=[(u,v) for u,v,w in edge_list[:-1]], 
                               width=3, edge_color='blue', ax=ax)
    
    u, v, w = edge_list[-1]
    nx.draw_networkx_edges(G, pos, edgelist=[(u,v)], width=5, edge_color='red', ax=ax)
    
    curr_weights = {(u,v): w for u,v,w in edge_list}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=curr_weights, font_size=9, ax=ax)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

print(f"Algorithm Complete. Total MST Cost = {total_cost}")