import networkx as nx
import matplotlib.pyplot as plt

G1 = nx.Graph()

G1.add_edges_from([
(1,2),(2,3),(3,4),(4,5),(5,6),(6,7),(7,8),(8,1),(1,7),
(1,3),(1,5),(2,8),(2,4),(2,6),(3,5),(3,7),(4,6),(4,8),(5,7),(6,8)
])

pos = {
1:(0,2),
2:(1.5,1.5),
3:(2,0),
4:(1.5,-1.5),
5:(0,-2),
6:(-1.5,-1.5),
7:(-2,0),
8:(-1.5,1.5)
}

SG = nx.Graph()
SG.add_nodes_from(G1.nodes())
SG.add_edges_from([
    (3,7),(2,6),(4,8),(5,1)
]) 

IGnodes = [1,2,3,4]

IG = nx.Graph()
IG.add_nodes_from(IGnodes)

for u,v in G1.edges():
    if u in IGnodes and v in IGnodes:
        IG.add_edge(u,v)


EIGedges = [(1,2),(2,3),(3,4),(4,5)]

EIG = nx.Graph()

for u,v in EIGedges:
    if G1.has_edge(u,v):
        EIG.add_edge(u,v)

plt.figure(figsize=(10,8))

plt.subplot(2,2,1)
nx.draw(G1,pos, with_labels=True, node_size=1000,node_color='lightblue')
plt.title("Original Graph")

plt.subplot(2,2,2)
nx.draw(SG,pos, with_labels=True, node_size=1000,node_color='lightgreen')
plt.title("Spanning Subgraph")

plt.subplot(2,2,3)
nx.draw(IG,pos, with_labels=True, node_size=1000,node_color='orange')
plt.title("Induced Subgraph")

plt.subplot(2,2,4)
nx.draw(EIG,pos, with_labels=True, node_size=1000,node_color='yellow')
plt.title("Edge Induced Subgraph")

plt.show()