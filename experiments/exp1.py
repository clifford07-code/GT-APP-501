import networkx as nx
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8))
plt.subplot(2,3,1)
G1 = nx.Graph()
G1.add_nodes_from([0,1,2,3,4])
nx.draw(G1, with_labels=True)
plt.title("N5 (Null Graph)")
plt.subplot(2,3,2)
G2 = nx.Graph()
nodes = [0,1,2,3,4,5]
G2.add_nodes_from(nodes)
for i in nodes:
    for j in nodes:
        if i < j:
            G2.add_edge(i,j)
nx.draw(G2, with_labels=True)
plt.title("K6 (Complete Graph)")
plt.subplot(2,3,3)
G3 = nx.Graph()
G3.add_nodes_from([0,1,2,3,4])
G3.add_edges_from([(0,1),(1,2),(2,3),(3,4)])
nx.draw(G3, with_labels=True)
plt.title("P5 (Path Graph)")
plt.subplot(2,3,4)
G4 = nx.Graph()
left = [0,1,2]
right = [3,4,5]
G4.add_nodes_from(left)
G4.add_nodes_from(right)
for i in left:
    for j in right:
        G4.add_edge(i,j)
pos = {}
pos.update((n,(1,i)) for i,n in enumerate(left))
pos.update((n,(2,i)) for i,n in enumerate(right))
nx.draw(G4, pos, with_labels=True)
plt.title("K(2,4) Bipartite Graph")
plt.subplot(2,3,5)
G5 = nx.Graph()
G5.add_edges_from([
(0,1),(1,2),(2,3),(3,4),
(4,5),(5,6),(6,7),(7,0)
])
pos = nx.circular_layout(G5)
nx.draw(G5, pos, with_labels=True)
plt.title("C8 (Cycle Graph)")
plt.subplot(2,3,6)
G6 = nx.Graph()
G6.add_edges_from([
(1,2),(2,3),(3,4),(4,5),(5,1)
])
G6.add_edges_from([
(0,1),(0,2),(0,3),(0,4),(0,5)
])
pos = nx.spring_layout(G6)
nx.draw(G6, pos, with_labels=True)
plt.title("W6 (Wheel Graph)")
plt.tight_layout()
plt.show()
