import networkx as nx
import matplotlib.pyplot as plt


G1 = nx.Graph()
G1.add_edges_from([
    (1, 2), (2, 3), (3, 4), (4, 1),
    (4, 2), (2, 5), (3, 5),
    (5, 6), (6, 1)
])


possquare = {
    1: (0, 1),
    2: (1, 1),
    3: (1, 0),
    4: (0, 0),
    5: (0.550, 0.900),
    6: (0.250, 0.600)
}

G2 = nx.Graph()
G2.add_edges_from([
    (1, 2), (2, 3), (3, 4), (4, 5),
    (5, 1), (1, 6), (6, 3),
    (4, 2), (2, 5)
])

pospentagon = {
    1: (0, 1),
    2: (0.95, 0.31),
    3: (0.59, -0.81),
    4: (-0.59, -0.81),
    5: (-0.95, 0.31),
    6: (-0.400, 0)
}


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
nx.draw(G1, possquare, with_labels=True, node_size=1500,node_color='lightblue')
plt.title("Graph G1")

plt.subplot(1, 2, 2)
nx.draw(G2, pospentagon, with_labels=True, node_size=1500,node_color='lightgreen')
plt.title("Graph G2 ")

plt.show()


print("Are G1 and G2 isomorphic?",
      nx.is_isomorphic(G1, G2))
