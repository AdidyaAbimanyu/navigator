import osmnx as ox
import matplotlib.pyplot as plt
import heapq

def load_graph(north, south, east, west):
    G = ox.graph_from_bbox(bbox=(north, south, east, west), network_type="drive")
        
    return G

def style_unvisited_edge(G, edge):
    G.edges[edge]["color"] = "#6a18Ad"
    G.edges[edge]["alpha"] = 0.2
    G.edges[edge]["linewidth"] = 0.5

def style_visited_edge(G, edge):
    G.edges[edge]["color"] = "#6a187d"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_active_edge(G, edge):
    G.edges[edge]["color"] = '#bb10e3'
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def style_path_edge(G, edge):
    G.edges[edge]["color"] = "white"
    G.edges[edge]["alpha"] = 1
    G.edges[edge]["linewidth"] = 1

def plot_graph(G, filename=None):
    fig, ax = ox.plot_graph(
        G,
        node_size=[G.nodes[node]["size"] for node in G.nodes],
        node_color="white",
        bgcolor="#18080e",
        edge_color=[G.edges[edge]["color"] for edge in G.edges],
        edge_alpha=[G.edges[edge]["alpha"] for edge in G.edges],
        edge_linewidth=[G.edges[edge]["linewidth"] for edge in G.edges],
        show=False
    )

    for node in G.nodes:
        if "label" in G.nodes[node]:
            x, y = G.nodes[node]["x"], G.nodes[node]["y"]
            ax.text(x, y, G.nodes[node]["label"], font='Arial', fontsize=10, color='white', ha='right')
    
    if filename:
        plt.savefig(filename)
        plt.close()  # Close the plot to release resources
    else:
        plt.show()

def distance(G, node1, node2):
    x1, y1 = G.nodes[node1]["x"], G.nodes[node1]["y"]
    x2, y2 = G.nodes[node2]["x"], G.nodes[node2]["y"]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def a_star(G, orig, dest, plot=False):
    for node in G.nodes:
        G.nodes[node]["previous"] = None
        G.nodes[node]["size"] = 0
        G.nodes[node]["g_score"] = float("inf")
        G.nodes[node]["f_score"] = float("inf")
    G.nodes[orig]["label"] = "Start"
    G.nodes[dest]["label"] = "Tempat Pengungsian"
    for edge in G.edges:
        style_unvisited_edge(G, edge)
    G.nodes[orig]["size"] = 50
    G.nodes[dest]["size"] = 50
    G.nodes[orig]["g_score"] = 0
    G.nodes[orig]["f_score"] = distance(G, orig, dest)
    pq = [(G.nodes[orig]["f_score"], orig)]
    step = 0
    while pq:
        _, node = heapq.heappop(pq)
        if node == dest:
            if plot:
                print("Iterations:", step)
                plot_graph(G)
            return
        for edge in G.out_edges(node):
            style_visited_edge(G, (edge[0], edge[1], 0))
            neighbor = edge[1]
            tentative_g_score = G.nodes[node]["g_score"] + distance(G, node, neighbor)
            if tentative_g_score < G.nodes[neighbor]["g_score"]:
                G.nodes[neighbor]["previous"] = node
                G.nodes[neighbor]["g_score"] = tentative_g_score
                G.nodes[neighbor]["f_score"] = tentative_g_score + distance(G, neighbor, dest)
                heapq.heappush(pq, (G.nodes[neighbor]["f_score"], neighbor))
                for edge2 in G.out_edges(neighbor):
                    style_active_edge(G, (edge2[0], edge2[1], 0))
        step += 1

def reconstruct_path(G, orig, dest, plot=False, algorithm=None):
    for edge in G.edges:
        style_unvisited_edge(G, edge)
    dist = 0
    curr = dest
    while curr != orig:
        prev = G.nodes[curr]["previous"]
        dist += G.edges[(prev, curr, 0)]["length"]
        style_path_edge(G, (prev, curr, 0))
        if algorithm:
            G.edges[(prev, curr, 0)][f"{algorithm}_uses"] = G.edges[(prev, curr, 0)].get(f"{algorithm}_uses", 0) + 1
        curr = prev
    dist /= 1000
    if plot:
        print(f"Distance: {dist}")
        plot_graph(G)
