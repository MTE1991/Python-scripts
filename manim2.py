from manim import *

class KeplerianOrbit(Scene):
    # Define the rate function to follow Kepler's 2nd Law
    def kepler_rate_func(self, t):
        # Calculate the mean anomaly
        M = 2 * np.pi * t
        # Solve Kepler's equation for the eccentric anomaly E
        E = M
        for _ in range(5):  # Iterate to improve accuracy
            E = M + 0.5 * np.sin(E)
        # Calculate the true anomaly
        theta = 2 * np.arctan(np.sqrt((1 + 0.5) / (1 - 0.5)) * np.tan(E / 2))
        # Normalize theta to be between 0 and 1
        return (theta + np.pi) / (2 * np.pi)

    def construct(self):
        # Create the elliptical orbit (width = 2a, height = 2b)
        two_a = 8
        two_b = 6
        ellipse = Ellipse(width=two_a, height=two_b)  # Semi-major axis = 4, semi-minor axis = 3

        # Create the Sun at the focus (at one of the foci of the ellipse)
        sun = Dot(ellipse.get_center() + LEFT * 2, color=YELLOW, radius=1)
        sun.scale(0.4)

        # Create a planet (representing a satellite, etc.)
        planet = Dot(color=RED, radius=1)
        planet.scale(0.1)

        for _ in range(2):
            # Create the motion path (ellipse)
            orbit_path = TracedPath(planet.get_center, stroke_opacity=[0, 1], stroke_color=GREY)

            # Add everything to the scene
            self.add(sun, planet, orbit_path)

            # Animate the planet moving along the orbit    
            self.play(MoveAlongPath(planet, ellipse), run_time=10, rate_func=self.kepler_rate_func)

        # Wait at the end
        self.wait(1)