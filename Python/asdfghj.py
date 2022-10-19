import matplotlib.pyplot as plt
import networkx as nx

G = nx.DiGraph()
G.add_nodes_from(range(5))
G.add_edge(0, 1, weight=1.0)
G.add_weighted_edges_from([(0, 2, 0.5), (1, 2, 0.75), (2, 3, 0.5), (3, 4, 0.5)])

fig, ax = plt.subplots()
pos = {0: (0, 0), 1: (1, 0), 2: (0.5, 1), 3: (0.5, 2), 4: (0.5, 3)}
nx.draw(G, ax=ax, pos=pos, with_labels=True)
ax.set_title("Sasfdghj")
plt.show()
