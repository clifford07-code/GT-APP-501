import matplotlib.pyplot as plt
import networkx as nx
import math
deg = list(map(int, input("Enter degree sequence: ").split()))
n = len(deg)
G = nx.Graph()
G.add_nodes_from(range(n))
graphs = []
titles = []
step = 1
while True:
    pairs = [(deg[i], i) for i in range(n)]
    pairs.sort(key=lambda x: (-x[0], x[1]))   
    print(f"\nStep {step}: {pairs}")
    d, v = pairs[0]
    if d == 0:
        print("Graph complete.")
        break
    pairs = pairs[1:]
    if d > len(pairs):
        print("Invalid degree sequence")
        break
    edges = []
    for i in range(d):
        degree, u = pairs[i]
        if degree == 0:
            print("Invalid degree sequence")
            break
        G.add_edge(v, u)
        edges.append(f"{v}-{u}")
        deg[u] -= 1
    deg[v] = 0
    graphs.append(G.copy())
    titles.append(f"Step {step}: {v} → {', '.join(edges)}")
    step += 1
cols = 3
rows = math.ceil(len(graphs) / cols)
fig, axes = plt.subplots(rows, cols, figsize=(12, 4 * rows))
axes = axes.flatten()
pos = nx.circular_layout(G)
for i in range(len(graphs)):
    nx.draw(graphs[i], pos, ax=axes[i],
            with_labels=True,
            node_color='skyblue',
            node_size=500)
    axes[i].set_title(titles[i])
for i in range(len(graphs), len(axes)):
    axes[i].axis('off') 
plt.suptitle("Havel-Hakimi Graph Construction", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.show()