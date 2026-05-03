import heapq
import math

import numpy as np
from manim import *


class AStarGPSRoutingMinimalFixed(Scene):
    def format_score(self, value):
        if value == float("inf"):
            return "∞"
        return f"{value:.1f}"

    def distance(self, a, b, coords):
        x1, y1 = coords[a]
        x2, y2 = coords[b]
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def heuristic(self, node, goal, coords):
        return self.distance(node, goal, coords)

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path

    def make_score_group(self, g, h, f):
        return VGroup(
            Text(f"g={self.format_score(g)}", font_size=16),
            Text(f"h={self.format_score(h)}", font_size=16),
            Text(f"f={self.format_score(f)}", font_size=16),
        ).arrange(DOWN, buff=0.03)

    def update_score(self, node, g_score, f_score, goal, coords, node_views):
        old_score = node_views[node]["score"]
        h_value = self.heuristic(node, goal, coords)

        new_score = self.make_score_group(g_score[node], h_value, f_score[node])
        new_score.move_to(old_score.get_center())

        self.play(Transform(old_score, new_score), run_time=0.35)

    def construct(self):
        self.camera.background_color = "#111111"

        coords = {
            "Home": (0, 0),
            "A": (2, 1),
            "B": (1, 4),
            "C": (4, 2),
            "D": (5, 5),
            "E": (7, 3),
            "Office": (8, 6),
        }

        roads = {
            "Home": ["A", "B"],
            "A": ["Home", "C", "D"],
            "B": ["Home", "D"],
            "C": ["A", "E"],
            "D": ["A", "B", "Office"],
            "E": ["C", "Office"],
            "Office": ["D", "E"],
        }

        start = "Home"
        goal = "Office"

        pos = {
            "Home": np.array([-5.5, -2.2, 0]),
            "A": np.array([-3.5, -1.0, 0]),
            "B": np.array([-4.3, 1.4, 0]),
            "C": np.array([-1.5, -0.4, 0]),
            "D": np.array([-0.4, 1.6, 0]),
            "E": np.array([1.7, -0.1, 0]),
            "Office": np.array([3.3, 1.8, 0]),
        }

        title = Text("A* GPS Routing", font_size=36, weight=BOLD).to_edge(UP)
        formula = MathTex("f(n)=g(n)+h(n)", font_size=38, color=YELLOW)
        formula.next_to(title, DOWN, buff=0.15)

        self.play(FadeIn(title), Write(formula), run_time=1)

        edge_lines = {}
        edge_labels = VGroup()
        used_edges = set()

        for u in roads:
            for v in roads[u]:
                edge_key = tuple(sorted((u, v)))

                if edge_key in used_edges:
                    continue

                used_edges.add(edge_key)

                line = Line(pos[u], pos[v], color=GRAY, stroke_width=4)
                edge_lines[edge_key] = line

                weight = round(self.distance(u, v, coords), 1)
                label = Text(str(weight), font_size=15, color=GRAY_B)
                label.move_to((pos[u] + pos[v]) / 2 + UP * 0.18)
                edge_labels.add(label)

        self.play(
            LaggedStart(
                *[Create(line) for line in edge_lines.values()], lag_ratio=0.08
            ),
            FadeIn(edge_labels),
            run_time=1.8,
        )

        node_views = {}
        node_group = VGroup()

        for node, p in pos.items():
            circle = Circle(radius=0.52, color=WHITE, stroke_width=3)
            circle.set_fill(GRAY_E, opacity=1)
            circle.move_to(p)

            name = Text(node, font_size=20, weight=BOLD)
            name.move_to(p)

            h_initial = self.heuristic(node, goal, coords)
            score = self.make_score_group(float("inf"), h_initial, float("inf"))
            score.next_to(circle, DOWN, buff=0.12)

            group = VGroup(circle, name, score)

            node_views[node] = {
                "circle": circle,
                "name": name,
                "score": score,
                "group": group,
            }

            node_group.add(group)

        self.play(FadeIn(node_group), run_time=1)

        start_label = Text("START", font_size=14, color=GREEN)
        start_label.next_to(node_views[start]["circle"], UP, buff=0.08)

        goal_label = Text("GOAL", font_size=14, color=RED)
        goal_label.next_to(node_views[goal]["circle"], UP, buff=0.08)

        self.play(FadeIn(start_label), FadeIn(goal_label), run_time=0.5)

        g_score = {node: float("inf") for node in coords}
        f_score = {node: float("inf") for node in coords}
        came_from = {}

        g_score[start] = 0
        f_score[start] = self.heuristic(start, goal, coords)

        open_heap = []
        heapq.heappush(open_heap, (f_score[start], start))

        open_set = {start}
        closed_set = set()

        self.update_score(start, g_score, f_score, goal, coords, node_views)

        self.play(
            node_views[start]["circle"].animate.set_fill(BLUE, opacity=1), run_time=0.4
        )

        self.wait(0.5)

        found = False

        while open_heap:
            current_f, current = heapq.heappop(open_heap)

            if current not in open_set:
                continue

            open_set.remove(current)

            self.play(
                node_views[current]["circle"].animate.set_fill(RED, opacity=1),
                run_time=0.45,
            )

            self.wait(0.25)

            if current == goal:
                found = True
                break

            for neighbor in roads[current]:
                edge_key = tuple(sorted((current, neighbor)))
                edge = edge_lines[edge_key]

                self.play(edge.animate.set_stroke(YELLOW, width=7), run_time=0.25)

                if neighbor in closed_set:
                    self.play(edge.animate.set_stroke(GRAY, width=4), run_time=0.2)
                    continue

                tentative_g = g_score[current] + self.distance(
                    current, neighbor, coords
                )

                if tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score[neighbor] = tentative_g + self.heuristic(
                        neighbor, goal, coords
                    )

                    self.update_score(
                        neighbor, g_score, f_score, goal, coords, node_views
                    )

                    heapq.heappush(open_heap, (f_score[neighbor], neighbor))
                    open_set.add(neighbor)

                    self.play(
                        node_views[neighbor]["circle"].animate.set_fill(
                            BLUE, opacity=1
                        ),
                        run_time=0.35,
                    )

                self.play(edge.animate.set_stroke(GRAY, width=4), run_time=0.2)

            closed_set.add(current)

            self.play(
                node_views[current]["circle"].animate.set_fill(ORANGE, opacity=1),
                run_time=0.4,
            )

            self.wait(0.3)

        if found:
            path = self.reconstruct_path(came_from, goal)

            path_edges = [
                tuple(sorted((path[i], path[i + 1]))) for i in range(len(path) - 1)
            ]

            final_anims = []

            for edge_key in path_edges:
                final_anims.append(
                    edge_lines[edge_key].animate.set_stroke(GREEN, width=9)
                )

            for node in path:
                final_anims.append(
                    node_views[node]["circle"].animate.set_fill(GREEN, opacity=1)
                )

            self.play(*final_anims, run_time=1.5)

            result = Text("Best Route: " + " → ".join(path), font_size=26, color=GREEN)

            cost = Text(f"Total Cost: {g_score[goal]:.1f}", font_size=22, color=YELLOW)

            result_group = VGroup(result, cost).arrange(DOWN, buff=0.15)
            result_group.to_edge(DOWN)

            self.play(FadeIn(result_group), run_time=0.8)

        else:
            fail = Text("No route found", font_size=28, color=RED)
            fail.to_edge(DOWN)
            self.play(FadeIn(fail))

        self.wait(3)
