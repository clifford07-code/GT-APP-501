import networkx as nx
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
plt.subplot(2,3,1)
G1 = nx.empty_graph(5)
nx.draw(G1, with_labels=True)
plt.title("N5 (Null Graph)")
plt.subplot(2,3,2)
G2 = nx.complete_graph(6)
nx.draw(G2, with_labels=True)
plt.title("K6 (Complete Graph)")
plt.subplot(2,3,3)
G3 = nx.path_graph(5)
nx.draw(G3, with_labels=True)
plt.title("P5 (Path Graph)")
plt.subplot(2,3,4)

G4= nx.complete_bipartite_graph(3, 4)

pos = {
    0: (-1, 1),
    1: (-1, 0),
    2: (-1, -1),

    3: (1, 1.5),
    4: (1, 0.5),
    5: (1, -0.5),
    6: (1, -1.5)
}


nx.draw(G4, pos, with_labels=True)
plt.title("K(2,4) Bipartite Graph")
plt.subplot(2,3,5)
G5 = nx.cycle_graph(8)
pos = nx.circular_layout(G5)
nx.draw(G5, pos, with_labels=True)
plt.title("C8 (Cycle Graph)")
plt.subplot(2,3,6)

G6 = nx.wheel_graph(6)

pos = nx.circular_layout(G6)

pos[0] = [0, 0]

nx.draw(G6, pos, with_labels=True)
plt.title("W6 (Wheel Graph)")
plt.tight_layout()
plt.show()