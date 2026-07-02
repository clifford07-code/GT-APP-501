import networkx as nx
import matplotlib.pyplot as plt
degree_sequence = [5,5,4,4,2,2,1,1]
if nx.is_graphical(degree_sequence):
    print("The given degree sequence is Graphical.")
else:
    print("The given degree sequence is NOT Graphical.")
G = nx.havel_hakimi_graph(degree_sequence)
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=1000)
plt.title("Graph Generated from Degree Sequence [3,3,2,2,2,2]")
plt.show()