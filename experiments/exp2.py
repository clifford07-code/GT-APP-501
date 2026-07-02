import itertools
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
import networkx as nx 
import itertools

def isomorphic(G1, G2):

    print("Number of vertices in G1:", G1.number_of_nodes())
    print("Number of vertices in G2:", G2.number_of_nodes())

    if G1.number_of_nodes() != G2.number_of_nodes():
        print(" Different number of vertices")
        return False, None

    print("Number of edges in G1:", G1.number_of_edges())
    print("Number of edges in G2:", G2.number_of_edges())

    if G1.number_of_edges() != G2.number_of_edges():
        print(" Different number of edges")
        return False, None

    deg1 = sorted([d for n, d in G1.degree()])
    deg2 = sorted([d for n, d in G2.degree()])

    print("Degree sequence of G1:", deg1)
    print("Degree sequence of G2:", deg2)

    if deg1 != deg2:
        print(" Degree sequences are different")
        return False, None

    cycles1 = sorted([len(c) for c in nx.cycle_basis(G1)])
    cycles2 = sorted([len(c) for c in nx.cycle_basis(G2)])

    print("Cycle lengths in G1:", cycles1)
    print("Cycle lengths in G2:", cycles2)

    if cycles1 != cycles2:
        print(" Cycle structures are different")
        return False, None

    nodes1 = list(G1.nodes())
    nodes2 = list(G2.nodes())

    print("\nChecking possible mappings...")

    for perm in itertools.permutations(nodes2):
        mapping = dict(zip(nodes1, perm))

        match = True
        for u, v in G1.edges():
            if not G2.has_edge(mapping[u], mapping[v]):
                match = False
                break

        if match:
            print("Graphs are Isomorphic")
            print("Mapping Found:", mapping)
            return True, mapping

    print(" No valid mapping found")
    return False, None

result = isomorphic(G1, G2)

print("\nFinal Result:", result)


plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
nx.draw(G1, possquare, with_labels=True, node_size=1500,node_color='lightblue')
plt.title("Graph G1")

plt.subplot(1, 2, 2)
nx.draw(G2, pospentagon, with_labels=True, node_size=1500,node_color='lightgreen')
plt.title("Graph G2 ")

plt.show()


