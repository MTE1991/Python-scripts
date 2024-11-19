from manim import *

class KeplerianOrbit(Scene):
    # Define the rate function to follow Kepler's 2nd Law
    def kepler_rate_func(self, t, eccentricity=0.5):
        # Calculate the mean anomaly
        M = 2 * np.pi * t
        # Solve Kepler's equation for the eccentric anomaly E using an iterative method
        E = M
        for _ in range(5):  # Iterate to improve accuracy
            E = M + eccentricity * np.sin(E)
        # Calculate the true anomaly
        theta = 2 * np.arctan(np.sqrt((1 + eccentricity) / (1 - eccentricity)) * np.tan(E / 2))
        # Normalize theta to be between 0 and 1
        return (theta + np.pi) / (2 * np.pi)

    def get_position(self, t, a=4, b=3):
        # Calculate the position of the planet on the ellipse
        angle = 2 * np.pi * self.kepler_rate_func(t)
        x = a * np.cos(angle)
        y = b * np.sin(angle)
        return np.array([x, y, 0])

    def get_velocity(self, t, a=4, b=3):
        # Approximate velocity vector using central differences
        dt = 0.01
        pos_now = self.get_position(t, a, b)
        pos_next = self.get_position(t + dt, a, b)
        velocity = (pos_next - pos_now) / dt
        return velocity

    def construct(self):
        # Create the elliptical orbit (width = 2a, height = 2b)
        two_a = 8
        two_b = 6
        a = two_a / 2
        b = two_b / 2
        ellipse = Ellipse(width=two_a, height=two_b)

        # Create the Sun at the focus (at one of the foci of the ellipse)
        sun = Dot(ellipse.get_center() + LEFT * 2, color=YELLOW, radius=1)
        sun.scale(0.4)

        # Create a planet (representing a satellite, etc.)
        planet = Dot(color=RED, radius=1)
        planet.scale(0.1)

        # Create the motion path (ellipse)
        orbit_path = TracedPath(planet.get_center, stroke_opacity=0.5, stroke_color=GREY)

        # Velocity and position vectors
        position_vector = always_redraw(
            lambda: Arrow(start=sun.get_center(), end=planet.get_center(), buff=0, color=BLUE)
        )
        velocity_vector = always_redraw(
            lambda: Arrow(
                start=planet.get_center(),
                end=planet.get_center() + 0.5 * self.get_velocity(self.time_tracker.get_value(), a, b),
                buff=0,
                color=GREEN
            )
        )

        # Time tracker
        self.time_tracker = ValueTracker(0)

        # Update the planet's position based on the time tracker
        planet.add_updater(
            lambda mob: mob.move_to(self.get_position(self.time_tracker.get_value(), a, b))
        )

        # Add everything to the scene
        self.add(sun, planet, orbit_path, position_vector, velocity_vector)

        # Animate the planet moving along the orbit
        self.play(self.time_tracker.animate.set_value(1), run_time=20, rate_func=linear)

        # Wait at the end
        self.wait(1)
