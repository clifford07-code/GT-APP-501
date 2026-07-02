import networkx as nx
import matplotlib.pyplot as plt
def is_safe(node, color, G, color_dict):
    for neighbor in G.neighbors(node):
        if neighbor in color_dict and color_dict[neighbor] == color: return False
    return True
def graph_coloring_backtracking(G, fixed_clues):
    color_dict = fixed_clues.copy()
    nodes = sorted(G.nodes())
    def backtrack(index):
        if index == len(nodes): return True
        node = nodes[index]
        if node in fixed_clues: return backtrack(index + 1)
        for color in range(4):
            if is_safe(node, color, G, color_dict):
                color_dict[node] = color
                if backtrack(index + 1): return True
                del color_dict[node]
        return False
    backtrack(0)
    return color_dict
G = nx.Graph()
row_straight, row_curved, col_straight, col_curved, block_edges = [], [], [], [], []
for r in range(4):
    for c in range(4): G.add_node((r, c))
for r1 in range(4):
    for c1 in range(4):
        for r2 in range(4):
            for c2 in range(4):
                if (r1, c1) < (r2, c2):
                    if r1 == r2:
                        if abs(c1 - c2) == 1:
                            row_straight.append(((r1, c1), (r2, c2)))
                        else:
                            row_curved.append(((r1, c1), (r2, c2)))
                    elif c1 == c2:
                        if abs(r1 - r2) == 1:
                            col_straight.append(((r1, c1), (r2, c2)))
                        else:
                            col_curved.append(((r1, c1), (r2, c2)))
                    elif (r1 // 2 == r2 // 2) and (c1 // 2 == c2 // 2):
                        block_edges.append(((r1, c1), (r2, c2)))
G.add_edges_from(row_straight + row_curved + col_straight + col_curved + block_edges)
fixed_clues = {
    (0, 2): 0,   
    (1, 1): 0,   
    (3, 2): 2    
}
solution = graph_coloring_backtracking(G, fixed_clues)
print("\nSolved Sudoku:\n")
for r in range(4): print([solution[(r, c)] + 1 for c in range(4)])
pos = {(r, c): (c, -r) for r in range(4) for c in range(4)}
palette = ["#FF6666", "#66B2FF", "#66FF66", "#FFFF66"]
colors = [palette[solution[node]] for node in G.nodes()]
labels = {node: str(solution[node] + 1) for node in G.nodes()}
fig, ax = plt.subplots(figsize=(10, 10))
fig.suptitle("Sudoku Solved Using Graph Coloring ", fontsize=16, fontweight="bold")
nx.draw_networkx_edges(G, pos, edgelist=row_straight, edge_color="crimson", width=1.5, alpha=0.7, ax=ax)
nx.draw_networkx_edges(G, pos, edgelist=col_straight, edge_color="seagreen", width=1.5, alpha=0.7, ax=ax)
nx.draw_networkx_edges(G, pos, edgelist=block_edges, edge_color="dodgerblue", width=1.5, alpha=0.8, ax=ax)
Gd = nx.DiGraph(G)
for u, v in row_curved:
    rad = 0.4 if u[0] < 2 else -0.4
    nx.draw_networkx_edges(Gd, pos, edgelist=[(u, v)], edge_color="crimson", width=1.5, alpha=0.8, connectionstyle=f"arc3,rad={rad}", arrows=True, arrowstyle="-", ax=ax)
for u, v in col_curved:
    rad = -0.4 if u[1] < 2 else 0.4
    nx.draw_networkx_edges(Gd, pos, edgelist=[(u, v)], edge_color="seagreen", width=1.5, alpha=0.8, connectionstyle=f"arc3,rad={rad}", arrows=True, arrowstyle="-", ax=ax)
nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=1000, edgecolors="black", linewidths=1.5, ax=ax)
nx.draw_networkx_labels(G, pos, labels, font_size=15, font_weight="bold", ax=ax)
ax.axis("off")
plt.tight_layout()
plt.show()