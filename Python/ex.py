import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])
G.add_weighted_edges_from([
    ("A", "B", 4),
    ("B", "D", 10),
    ("D", "F", 11),
    ("A", "C", 2),
    ("B", "C", 5),
    ("C", "E", 3),
    ("E", "D", 4)
])
fig, ax = plt.subplots()
pos = {
    "A": (0, 0),
    "B": (0.25, 0.5),
    "C": (0.3, -0.5),
    "D": (0.5, 0.5),
    "E": (0.5, -0.4),
    "F": (0.75, 0.1)
}
nx.draw(G, ax=ax, pos=pos, with_labels=True)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=nx.get_edge_attributes(G, "weight"))
plt.show()

print(nx.shortest_path(G, source="A", target="F", weight="weight"))
print(nx.shortest_path_length(G, source="A", target="F", weight="weight"))
