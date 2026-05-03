import heapq

from manim import *

# ── Palette ────────────────────────────────────────────────────────────────────
BG = "#080C14"
NODE_DEF = "#1A2235"
NODE_BORDER = "#2D3F5C"
NODE_OPEN = "#1A3A6B"
NODE_CLOSED = "#1E2535"
NODE_PATH = "#0B4A35"
NODE_START = "#4C1D95"
NODE_END = "#7F1D1D"
NODE_CUR = "#78350F"
EDGE_DEF = "#1E2D45"
EDGE_PATH = "#10B981"
C_START = "#A78BFA"
C_END = "#F87171"
C_CUR = "#FBBF24"
C_OPEN = "#60A5FA"
C_CLOSED = "#4B5563"
C_PATH = "#34D399"
C_G = "#FBBF24"  # amber  – g cost
C_H = "#7DD3FC"  # sky    – heuristic
C_F = "#F9A8D4"  # pink   – f = g+h
C_EDGE_W = "#334155"
PACKET_COL = "#FCD34D"

# ── Topology ───────────────────────────────────────────────────────────────────
NODES = {
    "S": (-5.2, 1.4),
    "A": (-3.0, 2.7),
    "B": (-2.8, 0.1),
    "C": (-0.6, 3.0),
    "D": (-0.4, 0.7),
    "E": (1.9, 2.3),
    "F": (1.7, -0.3),
    "G": (3.8, 1.7),
    "T": (5.3, 0.4),
}

EDGES = [
    ("S", "A", 4),
    ("S", "B", 3),
    ("A", "C", 3),
    ("A", "D", 5),
    ("B", "D", 2),
    ("B", "F", 6),
    ("C", "E", 4),
    ("C", "D", 2),
    ("D", "E", 3),
    ("D", "F", 4),
    ("E", "G", 2),
    ("E", "T", 7),
    ("F", "T", 5),
    ("F", "G", 3),
    ("G", "T", 2),
]

START, END = "S", "T"
SCALE = 0.76


def heuristic(a, b):
    ax, ay = NODES[a]
    bx, by = NODES[b]
    return round(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5, 1)


def astar_trace():
    g_cost = {n: float("inf") for n in NODES}
    g_cost[START] = 0
    came_from = {}
    open_heap = [(heuristic(START, END), START)]
    closed = set()
    steps = []
    adj = {n: [] for n in NODES}
    for u, v, w in EDGES:
        adj[u].append((v, w))
        adj[v].append((u, w))

    while open_heap:
        _, cur = heapq.heappop(open_heap)
        if cur in closed:
            continue
        closed.add(cur)
        open_now = {n for _, n in open_heap if n not in closed}
        steps.append(
            {
                "current": cur,
                "open": open_now,
                "closed": set(closed),
                "g": dict(g_cost),
            }
        )
        if cur == END:
            break
        for nb, w in adj[cur]:
            if nb in closed:
                continue
            tg = g_cost[cur] + w
            if tg < g_cost[nb]:
                came_from[nb] = cur
                g_cost[nb] = tg
                heapq.heappush(open_heap, (tg + heuristic(nb, END), nb))

    path, c = [], END
    while c in came_from:
        path.append(c)
        c = came_from[c]
    path.append(START)
    path.reverse()
    return steps, path, g_cost


STEPS, BEST_PATH, FINAL_G = astar_trace()
H_VAL = {n: heuristic(n, END) for n in NODES}

# Label placement: push the g/h/f tag to one side of the node
LABEL_OFFSETS = {
    "S": LEFT * 0.85,
    "A": UP * 0.70,
    "B": DOWN * 0.70,
    "C": UP * 0.70,
    "D": DOWN * 0.70,
    "E": UP * 0.70,
    "F": DOWN * 0.70,
    "G": UP * 0.70,
    "T": RIGHT * 0.85,
}


class AStarNetworkRouting(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.node_mobs = {}
        self.edge_lines = {}
        self.ghf_labels = {}  # name → VGroup of three Text mobs

        self._intro()
        self._build_graph()
        self._run_astar()
        self._reveal_path()
        self._send_packets()
        self._outro()

    # ── helpers ────────────────────────────────────────────────────────────────
    def _pos(self, name):
        x, y = NODES[name]
        return np.array([x * SCALE, y * SCALE, 0])

    def _ring_color(self, name, snap):
        if name == START:
            return C_START
        if name == END:
            return C_END
        if name == snap["current"]:
            return C_CUR
        if name in snap["closed"]:
            return C_CLOSED
        if name in snap["open"]:
            return C_OPEN
        return NODE_BORDER

    def _make_ghf(self, name, g_val=None, highlight=False):
        """Three-line label: g (amber), h (sky), f (pink)."""
        inf_str = "∞"
        g_v = g_val if g_val is not None else None
        h_v = H_VAL[name]
        f_v = round(g_v + h_v, 1) if g_v is not None else None

        g_str = f"g = {g_v:.0f}" if g_v is not None else f"g {inf_str}"
        h_str = f"h = {h_v:.1f}"
        f_str = f"f = {f_v:.1f}" if f_v is not None else f"f {inf_str}"

        gc = C_CUR if highlight else C_G
        fc = "#FF80AB" if highlight else C_F

        g_t = Text(g_str, font_size=10, color=gc)
        h_t = Text(h_str, font_size=10, color=C_H)
        f_t = Text(f_str, font_size=10, color=fc)
        # separator line between h and f
        return VGroup(g_t, h_t, f_t).arrange(DOWN, buff=0.055)

    # ── intro ──────────────────────────────────────────────────────────────────
    def _intro(self):
        title = Text("A*  Algorithm", font_size=52, color=C_PATH, weight=BOLD)
        sub = Text("Network Routing  &  Packet Switching", font_size=22, color=C_H)
        sub.next_to(title, DOWN, buff=0.3)
        VGroup(title, sub).move_to(ORIGIN)
        self.play(Write(title, run_time=1.2))
        self.play(FadeIn(sub, shift=UP * 0.2, run_time=0.7))
        self.wait(1.4)
        self.play(FadeOut(VGroup(title, sub), run_time=0.6))

    # ── build static graph ─────────────────────────────────────────────────────
    def _build_graph(self):
        # edges + weight labels
        for u, v, w in EDGES:
            p1, p2 = self._pos(u), self._pos(v)
            line = Line(
                p1, p2, stroke_color=EDGE_DEF, stroke_width=1.8, stroke_opacity=0.65
            )
            mid = (p1 + p2) / 2
            perp = np.array([-(p2 - p1)[1], (p2 - p1)[0], 0])
            n = np.linalg.norm(perp)
            off = perp / n * 0.20 if n > 1e-6 else UP * 0.20
            wlbl = Text(str(w), font_size=12, color=C_EDGE_W).move_to(mid + off)
            self.edge_lines[(u, v)] = line
            self.edge_lines[(v, u)] = line
            self.add(line, wlbl)

        # nodes + initial g/h/f labels
        node_anims = []
        for name in NODES:
            pos = self._pos(name)
            fill = (
                NODE_START if name == START else (NODE_END if name == END else NODE_DEF)
            )
            ring = C_START if name == START else (C_END if name == END else NODE_BORDER)
            circ = Circle(
                radius=0.28,
                fill_color=fill,
                fill_opacity=1,
                stroke_color=ring,
                stroke_width=2.2,
            )
            circ.move_to(pos)
            nlbl = Text(name, font_size=17, color=WHITE, weight=BOLD).move_to(pos)
            self.node_mobs[name] = VGroup(circ, nlbl)
            node_anims.append(GrowFromCenter(VGroup(circ, nlbl)))

            g_init = 0 if name == START else None
            ghf = self._make_ghf(name, g_val=g_init)
            ghf.move_to(pos + LABEL_OFFSETS[name])
            self.ghf_labels[name] = ghf
            self.add(ghf)

        self.play(AnimationGroup(*node_anims, lag_ratio=0.07, run_time=1.4))

        # colour key  (tiny, bottom-right)
        key = VGroup(
            self._key_dot(C_G, "g -> actual cost"),
            self._key_dot(C_H, "h -> heuristic"),
            self._key_dot(C_F, "f  = g + h"),
        ).arrange(RIGHT, buff=0.45)
        key.to_edge(DOWN, buff=0.22)
        self.play(FadeIn(key, run_time=0.7))
        self.key = key
        self.wait(0.6)

    def _key_dot(self, col, label):
        dot = Dot(radius=0.07, color=col)
        txt = Text(label, font_size=12, color=col)
        txt.next_to(dot, RIGHT, buff=0.10)
        return VGroup(dot, txt)

    # ── A* loop ────────────────────────────────────────────────────────────────
    def _run_astar(self):
        heading = Text("A*  Search", font_size=18, color=C_H)
        heading.to_edge(UP, buff=0.20)
        self.play(FadeIn(heading, run_time=0.5))
        self.heading = heading

        # step counter at bottom-left
        self.step_lbl = always_redraw(lambda: VMobject())  # placeholder
        for idx, snap in enumerate(STEPS):
            self._apply_step(snap, idx)

    def _apply_step(self, snap, idx):
        cur = snap["current"]

        # ── 1. colour rings & fills ──
        ring_anims = []
        for name in NODES:
            rc = self._ring_color(name, snap)
            ring_anims.append(
                self.node_mobs[name][0].animate.set_stroke(color=rc, width=2.8)
            )
            if name == cur:
                ring_anims.append(self.node_mobs[name][0].animate.set_fill(NODE_CUR))
            elif name in snap["closed"] and name not in (START, END):
                ring_anims.append(self.node_mobs[name][0].animate.set_fill(NODE_CLOSED))
            elif name in snap["open"] and name not in (START, END):
                ring_anims.append(self.node_mobs[name][0].animate.set_fill(NODE_OPEN))

        # ── 2. update g/h/f labels ──
        label_anims = []
        for name in NODES:
            g_val = snap["g"].get(name)
            if g_val == float("inf"):
                continue
            new_ghf = self._make_ghf(name, g_val=g_val, highlight=(name == cur))
            new_ghf.move_to(self._pos(name) + LABEL_OFFSETS[name])
            label_anims.append(Transform(self.ghf_labels[name], new_ghf))

        # ── 3. step counter ──
        step_txt = Text(
            f"step  {idx + 1} / {len(STEPS)}   ·   expanding  {cur}   ·   "
            f"g={snap['g'][cur]:.0f}   h={H_VAL[cur]:.1f}   f={snap['g'][cur] + H_VAL[cur]:.1f}",
            font_size=13,
            color=C_H,
        ).to_edge(DOWN, buff=0.22)

        self.play(
            *ring_anims,
            *label_anims,
            FadeOut(self.key, run_time=0.3),
            FadeIn(step_txt, run_time=0.4),
            run_time=0.75,
        )
        self.key = step_txt  # reuse slot so next step fades it out

        # ── 4. pulse ──
        c = self.node_mobs[cur][0]
        self.play(c.animate.scale(1.22), run_time=0.18)
        self.play(c.animate.scale(1 / 1.22), run_time=0.18)
        self.wait(0.55)  # ← longer pause so viewer can read the values

    # ── optimal path ──────────────────────────────────────────────────────────
    def _reveal_path(self):
        # recolour path nodes
        for name in BEST_PATH:
            fill = (
                NODE_START
                if name == START
                else (NODE_END if name == END else NODE_PATH)
            )
            ring = C_START if name == START else (C_END if name == END else C_PATH)
            self.node_mobs[name][0].set_fill(fill)
            self.node_mobs[name][0].set_stroke(color=ring, width=3)

        # draw path edges
        for i in range(len(BEST_PATH) - 1):
            u, v = BEST_PATH[i], BEST_PATH[i + 1]
            pl = Line(
                self._pos(u),
                self._pos(v),
                stroke_color=EDGE_PATH,
                stroke_width=4.5,
                stroke_opacity=0.95,
            )
            self.play(Create(pl), run_time=0.45)

        # turn path node labels green
        lbl_anims = []
        for name in BEST_PATH:
            new_ghf = self._make_ghf(name, g_val=FINAL_G[name], highlight=False)
            new_ghf[0].set_color(C_PATH)  # g in green
            new_ghf[2].set_color(C_PATH)  # f in green
            new_ghf.move_to(self._pos(name) + LABEL_OFFSETS[name])
            lbl_anims.append(Transform(self.ghf_labels[name], new_ghf))
        self.play(*lbl_anims, run_time=0.6)

        total = sum(
            w
            for u, v, w in EDGES
            if u in BEST_PATH
            and v in BEST_PATH
            and abs(BEST_PATH.index(u) - BEST_PATH.index(v)) == 1
        )
        cost_lbl = Text(
            f"{' → '.join(BEST_PATH)}     total cost  {total}",
            font_size=15,
            color=C_PATH,
        ).to_edge(DOWN, buff=0.22)
        self.play(FadeOut(self.key), FadeIn(cost_lbl, run_time=0.6))
        self.wait(1.8)
        self.cost_lbl = cost_lbl

    # ── packet forwarding ──────────────────────────────────────────────────────
    def _send_packets(self):
        new_h = Text("Packet Forwarding", font_size=18, color=C_H)
        new_h.to_edge(UP, buff=0.20)
        self.play(Transform(self.heading, new_h), FadeOut(self.cost_lbl, run_time=0.4))

        for col in [PACKET_COL, "#60A5FA", "#F87171"]:
            self._one_packet(col)
        self.wait(0.5)

    def _one_packet(self, col):
        dot = Dot(radius=0.14, color=col, fill_opacity=1)
        dot.move_to(self._pos(START))
        self.play(FadeIn(dot, scale=0.4, run_time=0.25))
        for hop in BEST_PATH[1:]:
            ring = self.node_mobs[hop][0]
            self.play(
                dot.animate.move_to(self._pos(hop)),
                ring.animate.set_stroke(color=col, width=4.5),
                run_time=0.55,
                rate_func=smooth,
            )
            rc = C_START if hop == START else (C_END if hop == END else C_PATH)
            self.play(ring.animate.set_stroke(color=rc, width=2.8), run_time=0.15)
        self.play(FadeOut(dot, scale=0.3, run_time=0.22))

    # ── outro ──────────────────────────────────────────────────────────────────
    def _outro(self):
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.9)
        items = (
            VGroup(
                Text("f(n) = g(n) + h(n)", font_size=38, color=C_PATH, weight=BOLD),
                Text("g(n) -> actual cost from source", font_size=20, color=C_G),
                Text("h(n) -> heuristic to destination", font_size=20, color=C_H),
                Text("f(n) -> priority for exploration", font_size=20, color=C_F),
                Text(
                    "Optimal when h(n) is admissible",
                    font_size=16,
                    color=C_H,
                    slant=ITALIC,
                ),
            )
            .arrange(DOWN, buff=0.38)
            .move_to(ORIGIN)
        )
        for mob in items:
            self.play(FadeIn(mob, shift=UP * 0.15, run_time=0.50))
        self.wait(2.0)
        self.play(FadeOut(items))
