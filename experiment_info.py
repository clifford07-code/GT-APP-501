EXPERIMENT_META = {
    1: {
        "title": "Basic graphs",
        "date": "3/2/26",
        "description": "To implement basic graphs such as complete graph, cycle graph, path graph and complete bipartite graph. ",
        "theory": """
A graph is a mathematical structure used to represent relationships between different
objects. A graph consists of a set of vertices (also called nodes) and a set of edges that
connect pairs of vertices. The vertices represent the objects, while the edges show how those
objects are related to each other. A graph is usually written as G = (V, E), where V is the set
of vertices and E is the set of edges. Graphs are widely used to model real-world systems
such as social networks, computer networks, road maps, and communication systems, making
them an important concept in mathematics and computer science.

Null Graph:In Graph theory, a null graph is a graph that has vertices but no edges connecting
them. This means none of the vertices are related to each other. If a graph has n vertices and
zero edges, it is called a null graph. It represents a situation where objects exist but there are
no relationships between them.
Complete Graph:A complete graph is a graph in which every pair of distinct vertices is
connected by exactly one edge. This means each vertex is directly connected to all other
vertices in the graph. A complete graph with n vertices is usually denoted as K. It
represents a fully connected network where every object has a direct relationship with every
other object.
Path Graph:A path graph is a graph where vertices are connected in a single straight
sequence. Each vertex (except the first and last) is connected to exactly two other vertices.
The first and last vertices are connected to only one vertex each. It looks like a straight line
and represents a simple route from one point to another without forming a loop.
Circular (Cycle) Graph:A circular graph, also called a cycle graph, is a graph in which the
vertices are connected in such a way that they form a closed loop. Each vertex is connected to
exactly two other vertices. Unlike a path graph, the first and last vertices are also connected,
forming a circle.
Bipartite Graph:A bipartite graph is a graph whose vertices can be divided into two distinct
sets such that edges only connect vertices from one set to the other set. There are no edges
between vertices within the same set. This type of graph is often used to represent
relationships between two different groups, such as students and courses.
Wheel Graph:A wheel graph is formed by connecting a single central vertex to all vertices of
a cycle graph. It looks like a wheel, where the outer cycle forms the rim and the central vertex
forms the hub. The edges connecting the center to the outer vertices are like spokes of a
wheel.

NetworkX
NetworkX is a Python library used for creating, analyzing, and working with graphs in
Python. It helps us study graph theory concepts using code. With NetworkX, we can create
different types of graphs (like directed, undirected, weighted), add nodes and edges, find
shortest paths, check connectivity, and perform many graph algorithms. It is widely used in
data science, computer networks, and research for analyzing complex networks.
Creating a Graph:In NetworkX, the function nx.Graph() is used to create a new empty
undirected graph in Python. This function does not require any parameters. It simply
initializes a graph object where we can later add nodes and edges. For example, G =
nx.Graph() creates an empty graph stored in the variable G.

""",
        "programs": {
            1: {
                "title": "without using built-in functions",
                "objective": "Build and visualize various graph families manually node-by-node and edge-by-edge using Matplotlib and NetworkX."
            },
            2: {
                "title": "using Built-in functions ",
                "objective": "Instantiate and display graph families using NetworkX's optimized built-in generator functions (e.g., complete_graph, complete_bipartite_graph)."
            }
        }
    },

    2: {
        "title": "Graph Isomorphism",
        "date": "10/2/26",
        "description": "To implement graph isomorphism verification in order to compare structural equivalence between two graphs. ",
        "theory": """
In graph theory, graph isomorphism refers to a situation where two graphs have the same structure, even though their drawings or vertex labels may be different. In simple words, two graphs are said to be isomorphic if one graph can be transformed into the other by renaming its vertices without changing the connections between them. The position or layout of the graph does not matter; only the adjacency between vertices is important.

Formally, two graphs G₁ and G₂ are said to be isomorphic if there exists a one-to-one and onto mapping (bijection)

f : V(G₁) → V(G₂)

such that two vertices u and v are adjacent in G₁ if and only if f(u) and f(v) are adjacent in G₂. This mapping preserves adjacency between vertices. If such a mapping exists, we write:

G₁ ≅ G₂

For example, consider a graph G₁ with vertex set {1, 2, 3, 4} and another graph G₂ with vertex set {A, B, C, D}. If there exists a mapping such as 1 → A, 2 → B, 3 → C, and 4 → D, and all the edges in G₁ correspond exactly to the edges in G₂ under this mapping, then the two graphs are isomorphic.

Number of Vertices and Edges: The first method to check isomorphism is by comparing the number of vertices and edges in both graphs. For two graphs to be isomorphic, they must have exactly the same number of vertices and the same number of edges. If one graph has more vertices or more edges than the other, then they cannot be isomorphic. This condition is necessary but not sufficient, meaning even if both numbers are equal, the graphs may still not be isomorphic.

Degree Sequence Method: Another important method is comparing the degree sequence of both graphs. The degree of a vertex is the number of edges connected to it. To apply this method, we find the degree of each vertex in both graphs and arrange them in ascending or descending order. If the degree sequences are different, then the graphs are not isomorphic. If they are the same, the graphs may be isomorphic, but we need further checking because equal degree sequences do not guarantee isomorphism.

Connected Components: The number of connected components in both graphs must also be the same. A connected component is a part of the graph where all vertices are connected directly or indirectly. If one graph is connected (all vertices reachable from one another) and the other is disconnected (split into separate parts), then they cannot be isomorphic. This is another necessary condition.

Cycles in the Graph: Checking cycles is also an important method. A cycle is a closed path where we start and end at the same vertex without repeating edges. If one graph contains a triangle (3-cycle) and the other does not, they are not isomorphic. Similarly, the number of cycles of different lengths (like 3-cycle, 4-cycle, etc.) must be the same in both graphs. The presence or absence of specific cycles helps in identifying structural differences.

Adjacency Matrix Method: The adjacency matrix method is a systematic way to check isomorphism. First, we write the adjacency matrix of both graphs. Then we try to rearrange the rows and columns of one matrix by renaming the vertices. If we can make both matrices identical after rearrangement, then the graphs are isomorphic. This method is more mathematical and useful for smaller graphs but becomes complex for large graphs.

Bijection or Mapping Method: The most reliable method is constructing an explicit mapping between vertices of the two graphs. In this method, we match a vertex from the first graph with a vertex in the second graph that has the same degree. Then we check whether their neighboring vertices also correspond correctly. If we can create a complete mapping where all adjacency relationships are preserved, then the graphs are isomorphic. This method is commonly used in exams for proving isomorphism step by step.

Algorithmic or Computer Method: For large graphs, checking isomorphism manually is very difficult. Therefore, computer algorithms are used to test all possible vertex mappings efficiently. These algorithms check whether adjacency is preserved under different permutations of vertices. This method is mainly used in practical applications and software tools where graphs are large and complex.

In practical applications, graph isomorphism can also be verified using built-in functions available in graph libraries such as the NetworkX library in Python. NetworkX provides a function called is_isomorphic() which automatically checks whether two graphs are structurally identical. This function compares the vertices and edges of both graphs and determines if a bijection exists between their vertex sets that preserves adjacency. If such a mapping exists, the function returns True, indicating that the graphs are isomorphic; otherwise, it returns False. This method is very useful for quickly verifying graph isomorphism in computational graph theory experiments and practical implementations.
""",
        "programs": {
            1: {
               "title": "without using built-in functions",
                "objective": "Implement a manual isomorphism check by verifying degree sequences, cycle structures, and iterating over all vertex permutations."
            },
            2: {
                 "title": "using Built-in functions ",
                "objective": "Verify isomorphism using NetworkX's built-in, highly optimized VF2 isomorphism matching algorithm."
            }
        }
    },

    3: {
        "title": "Subgraphs",
        "date": "17/2/26",
        "description": "To implement generation of various subgraphs such as induced subgraphs, spanning subgraphs and edge-deleted subgraphs.",
        "theory": """
In graph theory, a subgraph of a graph G is a graph formed from a subset of the vertices and a subset of the edges of G. If G = (V, E), then a graph H = (V′, E′) is called a subgraph of G if V′ ⊆ V and E′ ⊆ E, and every edge in E′ connects vertices that are in V′. In simple words, a subgraph is obtained by removing some vertices and/or some edges from the original graph without adding any new elements. The remaining structure must still satisfy the properties of a graph.

Spanning Subgraph: A spanning subgraph is a special type of subgraph that includes all the vertices of the original graph but may contain only some of its edges. If G = (V, E), then a subgraph H = (V, E′) is called a spanning subgraph if E′ ⊆ E and the vertex set remains the same as G. This means that no vertices are removed, but some edges can be removed. A common example is a spanning tree, which connects all the vertices of a connected graph using the minimum number of edges.

Induced Subgraph (Vertex-Induced Subgraph): An induced subgraph is formed by selecting a subset of vertices from the original graph and including all the edges between those vertices that are present in the original graph. If V′ ⊆ V, then the induced subgraph on V′ contains every edge in G that has both endpoints in V′. In other words, once the vertices are selected, all edges between them must be included. This type of subgraph preserves the exact relationships among the chosen vertices.

Edge-Induced Subgraph: An edge-induced subgraph is formed by selecting a subset of edges from the original graph and including all the vertices that are endpoints of those edges. If E′ ⊆ E, then the edge-induced subgraph contains those edges along with the vertices connected by them. Unlike vertex-induced subgraphs, here the edges are selected first, and the vertex set is determined automatically. This type of subgraph focuses mainly on a specific collection of edges and their incident vertices.

In NetworkX, different types of subgraphs can be generated using built-in functions. For example, an induced subgraph can be created using nx.induced_subgraph() by selecting a set of vertices, and an edge-induced subgraph can be created using nx.edge_subgraph() by selecting specific edges. These functions automatically generate the corresponding subgraphs while preserving the relationships between vertices and edges. Such built-in functions make it easier to construct and visualize different subgraphs during practical graph theory implementations.
""",
        "programs": {
            1: {
                "title": "Built-in Subgraph Extraction",
                "objective": "Extract and visualize spanning, induced, and edge-induced subgraphs using NetworkX's library functions."
            },
            2: {
                "title": "Manual Subgraph Extraction",
                "objective": "Compute and construct spanning, induced, and edge-induced subgraphs from scratch using basic loop filters."
            }
        }
    },

    4: {
        "title": "degree sequence( Havel-Hakimi )",
        "date": "23/2/26",
        "description": "To implement construction of a graph for a given degree sequence in order to realize there is a graphical sequence using Havel-Hakimi algorithm. ",
        "theory": """
A degree sequence of a graph is a list of the degrees of all the vertices in the graph, usually written in non-increasing order. The degree of a vertex is the number of edges incident to that vertex. For example, if a graph has five vertices with degrees 5, 5, 4, 4, 2, 2, 1, and 1, then the degree sequence is written as (5, 5, 4, 4, 2, 2, 1, 1).

Degree sequences are important in graph theory because they help in understanding the structure of a graph and in determining whether a graph with the given degrees can exist. A sequence that corresponds to at least one valid graph is called a graphical sequence. One important property of degree sequences is that the sum of all vertex degrees must be even, since each edge contributes two degrees (one to each of its endpoints).

To construct a graph from a given degree sequence, vertices are assigned according to the sequence, and edges are added so that each vertex attains its specified degree. One commonly used method for this purpose is the Havel–Hakimi process.

In this method, the degree sequence is first arranged in descending order. The vertex with the highest degree is then connected to the next highest-degree vertices equal to its degree value. After forming these connections, the degrees of the connected vertices are reduced by one. The sequence is then rearranged in non-increasing order, and the same process is repeated. If at any stage a negative degree appears or the construction becomes impossible, then the sequence is not graphical. If the sequence is eventually reduced to all zeros, then a valid graph corresponding to the given degree sequence has been successfully constructed.

In Python, the NetworkX library provides built-in functions to generate graphs from a degree sequence. The function is_graphical is used to check whether a given degree sequence is graphical (i.e., whether a valid graph can be constructed from it). If the sequence is valid, the function havel_hakimi_graph constructs a simple graph using the Havel–Hakimi algorithm.
""",
        "programs": {
            1: {
                 "title": "using Built-in functions ",
                "objective": "Check if a pre-defined degree sequence is graphical and automatically generate the corresponding graph using NetworkX."
            },
            2: {
                "title": "without using built-in functions",
                "objective": "Take a custom degree sequence from the user and construct/visualize the graph step-by-step following the Havel-Hakimi reduction.",
                "has_input": True,
                "input_widgets": [
                    {
                        "key": "degree",
                        "label": "Enter Degree Sequence (space-separated integers)",
                        "type": "text",
                        "default": "5 5 4 4 2 2 1 1",
                        "placeholder": "e.g. 5 5 4 4 2 2 1 1"
                    }
                ]
            }
        }
    },

    5: {
        "title": "Line Graphs",
        "date": "10/3/26",
        "description": "To implement conversion of a given graph into a line graph where each vertex represents an edge of the original graph, and adjacency reflects shared endpoints. ",
        "theory": """
A line graph of a graph G=(V,E), written as L(G), is obtained by converting edges into vertices. In this transformation, each edge of the original graph becomes a vertex in the new graph. Two vertices in L(G) are connected if the corresponding edges in G share a common endpoint (i.e., they are incident). In simple terms, if two edges of G meet at a vertex, then their corresponding vertices in L(G) will be adjacent.

To construct a line graph from an adjacency matrix A=[aij], we first identify all edges of G from the entries where aij=1 (considering only i<j for an undirected graph). Each edge vivj is then taken as a vertex in L(G). After this, we compare pairs of edges and check whether they have a common vertex. If two edges share at least one endpoint, then an edge is drawn between their corresponding vertices in L(G). Repeating this process for all pairs gives the complete line graph.

In practical implementations, especially using Python, the NetworkX library provides built-in support for generating line graphs efficiently. After creating the original graph from the adjacency matrix using standard graph construction methods, the line graph can be generated directly using the function nx.line_graph(G). This function automatically converts each edge of G into a node and establishes connections between nodes based on shared endpoints, thereby eliminating the need for manual comparison of edges. NetworkX also allows visualization of both the original graph and its line graph using functions like nx.draw(), which helps in better understanding the structural transformation.
""",
        "programs": {
            1: {
               "title": "without using built-in functions",
                "objective": "Build the line graph of a weighted graph manually from combinations of edges sharing endpoints."
            },
            2: {
                "title": "using Built-in functions ",
                "objective": "Construct and render a line graph using NetworkX's built-in `line_graph` utility."
            }
        }
    },

    6: {
        "title": "Minimum Spanning Tree (Kruskal's)",
        "date": "24/3/26",
        "description": "To implement finding the minimum spanning tree for a given graph using Kruskal's algorithm, ensuring all vertices are connected with the minimum possible total edge weight and without forming cycles",
        "theory": """
A spanning tree of a connected graph G=(V,E) is a subgraph T=(V,ET) that includes all the vertices of G and is a tree (i.e., it is connected and has no cycles). A spanning tree has exactly ∣V∣−1 edges. In simple terms, it connects all the vertices of the graph using the minimum number of edges without forming any cycle.

A minimum spanning tree (MST) is defined for a weighted connected graph. It is a spanning tree whose total edge weight is minimum among all possible spanning trees of the graph. That is, if T is a spanning tree, then it is a minimum spanning tree if the sum of weights of edges in T is as small as possible.

Kruskal's Algorithm
● Step 1. Choose a link e, such that w(e₁) is as small as possible.

● Step 2. If edges ei, e2,..., e, have been chosen, then choose an edge ei+1 from E\{e1, e2,..., e} in such a way that

(i) G[{e1, e2,..., ei+1}] is acyclic;

(ii) w(e+1) is as small as possible subject to (i).

● Step 3. Stop when step 2 cannot be implemented further.
""",
        "programs": {
            1: {
                "title": "without using built-in functions",
                "objective": "Implement Kruskal's algorithm manually using Union-Find and visualize the step-by-step inclusion/highlighting of MST edges."
            },
            2: {
                "title": "using Built-in functions ",
                "objective": "Compute the Minimum Spanning Tree using NetworkX's built-in minimum spanning tree functions."
            }
        }
    },

    7: {
        "title": "Shortest Paths (Dijkstra's)",
        "date": "31/3/26",
        "description": "To implement shortest path algorithm in order to compute shortest path from the source vertex to all the vertices in a weighted graph.",
        "theory": """
Dijkstra’s Algorithm is a method used in graph theory to find the shortest path from a starting point to all other points in a network with non-negative distances. It works by repeatedly choosing the nearest unvisited point and updating the shortest known distances to its neighboring points. This approach ensures that the minimum distance to each point is found efficiently. It is widely used in real-world applications like navigation systems, network routing, and pathfinding in games.

Dijkstra's Algorithm
1. Set l(uo) =0, 1(v) = ∞ for v≠ uo, So={uo} and i = 0.
2. For each veS, replace l(v) by min{l(v), l(u,) + w(u,v)}. Compute min{l(v)} and let 1 denote a vertex for which this minimum is attained. Set Si+1= S; U{ui+1}.
3. If i= v - 1, stop. If i < v− 1, replace i by i+1 and go to step 2
""",
        "programs": {
            1: {
                "title": "using Built-in functions ",
                "objective": "Find shortest paths and total costs from a single source node using NetworkX's built-in Dijkstra solver."
            },
            2: {
               "title": "without using built-in functions",
                "objective": "Implement Dijkstra's algorithm from scratch and plot the tree relaxation process step-by-step."
            }
        }
    },

    8: {
        "title": "Walks, Trails, Paths, and Cycles",
        "date": "7/4/26",
        "description": "To implement generation of closed walks, trails and paths ina connected graph. ",
        "theory": """
A closed walk is a sequence of vertices and edges in which you start and end at the same vertex. In a walk, both vertices and edges can be repeated, meaning you are allowed to revisit the same node or edge multiple times. The only requirement for a closed walk is that the starting and ending vertex must be the same. Closed walks are useful in studying cycles and network flows, and they form the basis for more restricted structures like circuits. For example, if you move from vertex A → B → C → A, you have a closed walk because you return to the starting point.

A trail is a walk in which no edge is repeated, although vertices may be repeated. This means you can pass through the same vertex more than once, but you cannot use the same edge again. Trails are important in problems where each connection must be used at most once, such as in route planning or network traversal. An example of a trail is A → B → C → D → B, where the vertex B appears twice, but all edges are different.

A path is a more restricted form of a trail in which neither edges nor vertices are repeated. This means every vertex is visited only once, making it the simplest and most direct route between two points in a graph. Paths are widely used in shortest path problems and routing algorithms because they avoid loops and redundancy. For example, A → B → C → D is a path since all vertices and edges are distinct.

In NetworkX, The function networkx.cycle_basis(G) is used to compute a list of fundamental cycles in an undirected graph, where each cycle is represented as a list of nodes forming a closed path. It returns a minimal set of simple cycles from which all other cycles in the graph can be derived.
""",
        "programs": {
            1: {
                 "title": "using Built-in functions ",
                "objective": "Differentiate between closed paths, trails, and walks on graphs using NetworkX fundamental cycles (cycle basis)."
            },
            2: {
                "title": "without using built-in functions",
                "objective": "Find cycles and construct closed walks, trails, and paths using manual DFS backtracking."
            }
        }
    },

    9: {
        "title": "Eulerian Graphs & Circuits",
        "date": "28/4/26",
        "description": "To implement an algorithm that checks for the existence of an Eulerian circuit and construct a circuit that traverses every edge of the graph exactly once",
        "theory": """
An Eulerian circuit is a path in a graph that starts and ends at the same vertex while visiting every edge exactly once. This concept comes from graph theory and is used to determine whether it is possible to traverse all connections in a network without repeating any edge. A graph has an Eulerian circuit only if it is connected and every vertex has an even degree (i.e., an even number of edges connected to it). A classic example is the Seven Bridges of Königsberg problem, which led to the discovery of Eulerian circuits by Leonhard Euler.

Fleury’s Algorithm
S1: Choose an arbitrary vertex v0 and set W0= v0
S2: Suppose that the trail Wi=v0 ,e1 ,v1 ,e2 ,v2 ,…,ei ,vi has been chosen. Then choose an edge ei+1 from E∖{e1 ,e2 ,…,ei} such that:
i) ei+1 is incident with vi
ii) Unless there is no alternative, ei+1 is not a cut edge (bridge) of Gi = G−{e1 ,e2 ,…,ei}
S3:Stop when S2 can no longer be implemented

Function used to check eulerian circuit
In NetworkX, there are built-in functions to check and work with Eulerian circuits. The function nx.is_eulerian(G) is used to determine whether a given graph is Eulerian or not. It returns True if the graph contains an Eulerian circuit and False otherwise. Internally, it checks two important conditions: the graph must be connected (ignoring isolated vertices), and all vertices must have an even degree. However, this function only verifies the existence of an Eulerian circuit and does not return the actual path. To obtain the circuit, nx.eulerian_circuit(G) is used. This function returns a sequence of edges that forms an Eulerian circuit, meaning it starts and ends at the same vertex while visiting every edge exactly once. It works only when the graph satisfies Eulerian conditions. If the graph is not Eulerian, this function cannot be applied. Thus, NetworkX provides simple and efficient built-in functions to both check and generate Eulerian circuits in graphs.
""",
        "programs": {
            1: {
                "title": "Eulerian Status Check (Built-in)",
                "objective": "Verify if a graph is Eulerian and print the circuit path using NetworkX built-in methods."
            },
            2: {
                "title": "Manual Eulerian Solver & Visualizer",
                "objective": "Manually check connectivity and node degrees, then trace and animate the Eulerian circuit traversal step-by-step."
            }
        }
    },

    10: {
        "title": "Hamiltonian Circuits",
        "date": "5/5/26",
        "description": "To implement a method that determines whether a graph contains a Hamiltonian circuit i.e. a cycle that visits every vertex exactly once",
        "theory": """
Let ( G = (V, E) ) be a finite, connected, undirected graph, where ( V ) is the set of vertices and ( E ) is the set of edges.
A Hamiltonian circuit is a closed cycle in a graph that visits every vertex exactly once and returns to the starting vertex. The sequence of vertices in a Hamiltonian circuit can be represented as:
v0 ,v1 ,v2,…,vn−1 ,vn
such that:
1. ( v0 = vn ), which means the circuit starts and ends at the same vertex.
2. Every pair of consecutive vertices ( (vi-1 , vi) ) is connected by an edge in the graph.
3. Each vertex is visited exactly once except the starting vertex, which is repeated at the end to complete the cycle.
4. All vertices of the graph are included in the circuit.


A graph that contains a Hamiltonian circuit is called a Hamiltonian graph.
The main objective of a Hamiltonian circuit is to traverse every vertex exactly once and finally return to the starting point. Unlike Eulerian circuits, which focus on visiting every edge exactly once, Hamiltonian circuits focus on visiting every vertex exactly once.
In a Hamiltonian circuit, repetition of vertices is not allowed because the circuit must pass through each vertex only one time. The only repeated vertex is the starting vertex, which appears again at the end to form a closed cycle.
Hamiltonian circuits are widely used in applications such as route optimization, scheduling, computer networks, robotics, and DNA sequencing. One of the most famous problems related to Hamiltonian circuits is the Travelling Salesman Problem (TSP), where a salesman must visit each city exactly once and return to the starting city with minimum cost or distance.
A Hamiltonian path is a path that visits every vertex exactly once but does not return to the starting vertex. If the path forms a closed loop, then it becomes a Hamiltonian circuit. Hamiltonian circuits play an important role in graph theory because they help solve many real-world optimization and traversal problems involving efficient movement through connected systems and networks.
""",
        "programs": {
            1: {
                "title": "Hamiltonian Search via Backtracking",
                "objective": "Search for Hamiltonian circuits using a recursive backtracking algorithm and show the progress step-by-step."
            },
            2: {
                "title": "Hamiltonian Steps Visualizer",
                "objective": "Visualize pre-defined Hamiltonian cycles on complex grids to demonstrate path coverage."
            }
        }
    },

    11: {
        "title": "Greedy Vertex Coloring",
        "date": "12/5/26",
        "description": "To implement the greedy graph coloring that assigns colors to the vertices such that no two adjacent vertices share the same color with minimal chromatic number. ",
        "theory": """
Vertex Coloring
Vertex Coloring is a technique in Graph Theory where colors are assigned to the vertices (nodes) of a graph in such a way that no two adjacent vertices have the same color.
In mathematical form, if two vertices u and v are connected by an edge (u,v), then:
c(u) ≠ c(v)
where:
• c(u) = color assigned to vertex u
• c(v) = color assigned to vertex v
The main objective of vertex coloring is to use the minimum number of colors possible. The minimum number of colors required to color a graph G is called the Chromatic Number and is represented by:
χ(G)

Greedy Algorithm for Vertex Coloring
The Greedy Coloring Algorithm is a simple method used to color the vertices of a graph one by one.
Let:
G = (V,E)
where:
• V = set of vertices
• E = set of edges
The algorithm assigns the smallest possible color to each vertex such that no adjacent vertices receive the same color.
For a vertex vi, the assigned color is:
c(vi) = min {k ∈ N | k not in Adj(vi)}
where:
• Adj(vi) represents the colors used by adjacent vertices of vi
• k is the smallest available color
The greedy method may not always produce the optimal chromatic number χ(G), but it gives a fast and efficient approximate solution.

Steps of Greedy Vertex Coloring Algorithm
1. Initially, all vertices of the graph are uncolored.
2. Select the first vertex from the graph.
3. Assign the first available color to the selected vertex.
4. Move to the next vertex.
5. Check the colors assigned to all adjacent vertices.
6. Assign the smallest color that is not used by its neighboring vertices.
7. Repeat the process until all vertices are colored.
""",
        "programs": {
            1: {
                 "title": "using Built-in functions ",
                "objective": "Color a complex structural network using NetworkX's built-in DSATUR coloring heuristic."
            },
            2: {
                "title": "without using built-in functions",
                "objective": "Implement the DSATUR sorting and saturation assignment algorithm from scratch and draw the colored graph."
            },
            3: {
                "title": "Sudoku Solver via Graph Coloring",
                "objective": "Model a 4x4 Sudoku board as a 16-node graph coloring problem and solve/render it using backtracking and graph visualization."
            }
        }
    }
}