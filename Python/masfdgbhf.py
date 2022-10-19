import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

# G.add_node(1)
# G.add_node(2)
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G", "H"])
# G.add_nodes_from([3, 4, 5, 6, 7])
# G.add_edge(1, 2)
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E"), ("D", "F"), ("E", "F")])

fig, ax = plt.subplots()
layout = nx.shell_layout(G)
nx.draw(G, ax=ax, pos=layout, with_labels=True)
ax.set_title("Shell Layout sdfghgjh")
# plt.plot(G.nodes(), G.edges())
plt.show()
print(nx.info(G))

for i in ["A", "B", "E"]:
    degree = G.degree(i)
    print("Degree of node", i, "is", degree)

print(list(nx.connected_components(G)))
print(nx.density(G))
is_planar, _ = nx.check_planarity(G)
print("is planar -> ", is_planar)

print(nx.to_scipy_sparse_matrix(G))
print(nx.to_scipy_sparse_matrix(G).todense())

# print(G.nodes()) # []
# print(G.edges()) # []
# print(type(G.nodes())) # <class 'networkx.classes.reportviews.NodeView'>
# print(type(G.edges())) # <class 'networkx.classes.reportviews.EdgeView'>
