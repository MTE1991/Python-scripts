import heapq
import math

import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.animation import FuncAnimation

# ---------------------------------------------------
# 1. Define expanded map graph (GPS-like road network)
# ---------------------------------------------------
graph = {
    "Dhaka": {"Gazipur": 80, "Narayanganj": 70, "Savar": 45},
    "Gazipur": {"Dhaka": 80, "Mymensingh": 120, "Tangail": 90},
    "Narayanganj": {"Dhaka": 70, "Tangail": 100},
    "Savar": {"Dhaka": 45, "Manikganj": 65, "Tangail": 110},
    "Manikganj": {"Savar": 65, "Pabna": 160, "Sirajganj": 140},
    "Tangail": {
        "Gazipur": 90,
        "Narayanganj": 100,
        "Savar": 110,
        "Sirajganj": 100,
        "Rajshahi": 130,
    },
    "Mymensingh": {"Gazipur": 120, "Bogura": 180, "Rajshahi": 200},
    "Sirajganj": {"Tangail": 100, "Manikganj": 140, "Bogura": 90, "Rajshahi": 150},
    "Pabna": {"Manikganj": 160, "Rajshahi": 100},
    "Bogura": {"Mymensingh": 180, "Sirajganj": 90, "Rajshahi": 110},
    "Rajshahi": {
        "Tangail": 130,
        "Mymensingh": 200,
        "Sirajganj": 150,
        "Pabna": 100,
        "Bogura": 110,
    },
}

# ---------------------------------------------------
# 2. Make sure the graph is undirected
# ---------------------------------------------------
for u in list(graph.keys()):
    for v, w in list(graph[u].items()):
        if v not in graph:
            graph[v] = {}

        if u not in graph[v]:
            graph[v][u] = w

# ---------------------------------------------------
# 3. Position of each city for plotting
#    These act like map coordinates
# ---------------------------------------------------
positions = {
    "Dhaka": (0, 0),
    "Gazipur": (2, 2),
    "Narayanganj": (2, -2),
    "Savar": (1.5, -0.5),
    "Manikganj": (3.5, -1.5),
    "Tangail": (5, 0),
    "Mymensingh": (5, 3),
    "Sirajganj": (7, 1),
    "Pabna": (7, -2),
    "Bogura": (8, 3),
    "Rajshahi": (10, 0),
}

start = "Dhaka"
goal = "Rajshahi"


# ---------------------------------------------------
# 4. Heuristic function
#    Straight-line distance to the goal
# ---------------------------------------------------
def heuristic(node, goal):
    x1, y1 = positions[node]
    x2, y2 = positions[goal]

    straight_line_distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    # Multiplied by 40 to make the heuristic similar to road distance scale
    return straight_line_distance * 40


# ---------------------------------------------------
# 5. Reconstruct the final path
# ---------------------------------------------------
def reconstruct_path(came_from, current):
    path = [current]

    while current in came_from:
        current = came_from[current]
        path.append(current)

    path.reverse()
    return path


# ---------------------------------------------------
# 6. A* algorithm with state recording for visualization
# ---------------------------------------------------
def a_star_visual(graph, start, goal):
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, goal), start))

    came_from = {}

    g_cost = {}
    f_cost = {}

    for node in graph:
        g_cost[node] = float("inf")
        f_cost[node] = float("inf")

    g_cost[start] = 0
    f_cost[start] = heuristic(start, goal)

    open_set = {start}
    closed_set = set()

    # This list stores every step of the algorithm
    steps = []

    while open_heap:
        current_f, current = heapq.heappop(open_heap)

        if current not in open_set:
            continue

        open_set.remove(current)

        # Save current state before expanding the node
        steps.append(
            {
                "current": current,
                "open_set": set(open_set),
                "closed_set": set(closed_set),
                "came_from": dict(came_from),
                "g_cost": dict(g_cost),
                "f_cost": dict(f_cost),
                "final_path": None,
                "message": f"Expanding node: {current}",
            }
        )

        # If goal is reached, reconstruct final path
        if current == goal:
            path = reconstruct_path(came_from, current)

            steps.append(
                {
                    "current": current,
                    "open_set": set(open_set),
                    "closed_set": set(closed_set),
                    "came_from": dict(came_from),
                    "g_cost": dict(g_cost),
                    "f_cost": dict(f_cost),
                    "final_path": path,
                    "message": "Goal reached! Final path found.",
                }
            )

            return path, g_cost[goal], steps

        closed_set.add(current)

        # Check all neighboring cities
        for neighbor, distance in graph[current].items():
            if neighbor in closed_set:
                continue

            tentative_g = g_cost[current] + distance

            # If a better route to the neighbor is found
            if tentative_g < g_cost[neighbor]:
                came_from[neighbor] = current

                g_cost[neighbor] = tentative_g
                f_cost[neighbor] = tentative_g + heuristic(neighbor, goal)

                heapq.heappush(open_heap, (f_cost[neighbor], neighbor))
                open_set.add(neighbor)

                steps.append(
                    {
                        "current": current,
                        "open_set": set(open_set),
                        "closed_set": set(closed_set),
                        "came_from": dict(came_from),
                        "g_cost": dict(g_cost),
                        "f_cost": dict(f_cost),
                        "final_path": None,
                        "message": f"Updated neighbor: {neighbor}",
                    }
                )

    return None, float("inf"), steps


# ---------------------------------------------------
# 7. Run A*
# ---------------------------------------------------
path, total_cost, steps = a_star_visual(graph, start, goal)

print("Best Path:", path)
print("Total Cost:", total_cost)

# ---------------------------------------------------
# 8. Build NetworkX graph for drawing
# ---------------------------------------------------
G = nx.Graph()

for u in graph:
    for v, w in graph[u].items():
        G.add_edge(u, v, weight=w)

edge_labels = nx.get_edge_attributes(G, "weight")

# ---------------------------------------------------
# 9. Visualization / Animation
# ---------------------------------------------------
fig, ax = plt.subplots(figsize=(14, 8))


def draw_step(step_data):
    ax.clear()

    current = step_data["current"]
    open_set = step_data["open_set"]
    closed_set = step_data["closed_set"]
    final_path = step_data["final_path"]
    message = step_data["message"]
    g_cost = step_data["g_cost"]
    f_cost = step_data["f_cost"]

    # Assign color to each node
    node_colors = []

    for node in G.nodes():
        if node == start:
            node_colors.append("lightgreen")
        elif node == goal:
            node_colors.append("lightcoral")
        elif node == current:
            node_colors.append("gold")
        elif node in open_set:
            node_colors.append("orange")
        elif node in closed_set:
            node_colors.append("skyblue")
        else:
            node_colors.append("lightgray")

    # Draw the graph
    nx.draw(
        G,
        positions,
        with_labels=True,
        node_color=node_colors,
        node_size=1800,
        font_size=9,
        font_weight="bold",
        ax=ax,
    )

    # Draw road distance labels
    nx.draw_networkx_edge_labels(
        G,
        positions,
        edge_labels=edge_labels,
        font_size=8,
        ax=ax,
    )

    # Highlight the final path
    if final_path:
        path_edges = list(zip(final_path[:-1], final_path[1:]))

        nx.draw_networkx_edges(
            G,
            positions,
            edgelist=path_edges,
            width=4,
            edge_color="green",
            ax=ax,
        )

    # Show g(n) and f(n) values below each node
    for node, (x, y) in positions.items():
        g_val = g_cost.get(node, float("inf"))
        f_val = f_cost.get(node, float("inf"))

        if g_val == float("inf"):
            g_text = "∞"
        else:
            g_text = f"{g_val:.0f}"

        if f_val == float("inf"):
            f_text = "∞"
        else:
            f_text = f"{f_val:.0f}"

        ax.text(
            x,
            y - 0.55,
            f"g={g_text}, f={f_text}",
            fontsize=8,
            ha="center",
            bbox=dict(facecolor="white", alpha=0.7, edgecolor="none"),
        )

    ax.set_title(f"A* Algorithm for GPS Route Planning\n{message}", fontsize=14)

    ax.axis("off")


# ---------------------------------------------------
# 10. Animation update function
# ---------------------------------------------------
def update(frame):
    draw_step(steps[frame])


# ---------------------------------------------------
# 11. Create and save animation
# ---------------------------------------------------
ani = FuncAnimation(fig, update, frames=len(steps), interval=1500, repeat=False)

ani.save("a_star_routing_expanded.gif", writer="pillow", fps=0.5)

print("Animation saved as a_star_routing_expanded.gif")
