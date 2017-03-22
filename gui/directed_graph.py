import networkx as nx
import pylab

"""
|-------------------------------------------------------------------------------
| Directed Graph GUI
|-------------------------------------------------------------------------------
|
| This visualises the transitions found in a digraph. It uses a library which
| isn't particularly good at visualising graphs which plenty of nodes, so
| in circumstances where you expect there to be plenty of transitions,
| this visualisation is of limited use.
|
"""

def plot_loops(loops):
    G = nx.DiGraph()
    val_map = {}
    node_values = []
    trivial_edges = []

    for i in range(0, len(loops)):
        loop = loops[i]
        G.add_edges_from([(str(loop[0]), str(loop[1]))], weight=int(loop[2]))
        val_map[loop[0]] = loop[3]

    for i in range(0, len(loops)):
        node_values.append(loops[i][0])
        node_values.append(loops[i][1])

    node_values = list(set(node_values))
    node_values.sort()

    for i in range(0, len(node_values) - 1):
        weight = abs(node_values[i] - node_values[i + 1])
        G.add_edges_from([(str(node_values[i]), str(node_values[i + 1]))], weight=weight)
        trivial_edges.append((str(node_values[i]), str(node_values[i + 1])))

    # Set the edges to be green if going forwards, and red if going backwards
    edge_colours = ['red' if not edge in trivial_edges else 'green'
                    for edge in G.edges()]

    # Label the edges with the frame distance of the transition
    edge_labels = dict([((u, v,), d['weight'])
                        for u, v, d in G.edges(data=True)])

    # Use the graph library to output the visualisation
    pos = nx.circular_layout(G)
    node_labels = {node: node for node in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=node_labels)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    nx.draw(G, pos, node_color="#cee3f8", edge_color=edge_colours, node_size=1000)
    pylab.title('Digraph for image traversal')
    pylab.show()
