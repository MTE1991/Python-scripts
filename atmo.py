from manim import *
import numpy as np
from scipy.optimize import curve_fit  

class AltitudePressurePlot(Scene):
    def construct(self):
        # Sample data for elevation (in meters) and air pressure (in pascals) for the troposphere
        altitudes = np.array([0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])  # Altitudes in meters
        pressures = np.array([101325, 89874, 79502, 70123, 61658, 54068, 47342, 41471, 36446, 32152, 28663])  # Pressure in pascals

        # Exponential model function
        def exponential_model(h, P0, k):
            return P0 * np.exp(-k * h)

        # Fit the data to the exponential model
        params, covariance = curve_fit(exponential_model, altitudes, pressures, p0=[101325, 0.0001])

        # Extract the fitted parameters
        P0_fit, k_fit = params

        # Generate the fitted curve
        altitudes_fine = np.linspace(0, 10000, 500)  # Smooth range of altitudes for plotting
        pressures_fitted = exponential_model(altitudes_fine, P0_fit, k_fit)

        # Calculate the pressure at 5 km (5000 meters)
        pressure_at_5km = exponential_model(5000, P0_fit, k_fit)

        # Create axes
        axes = Axes(
            x_range=[0, 11000, 1000],
            y_range=[20, 120, 10],
            x_axis_config={"color": GREEN, "include_numbers": True},  # Set x-axis color to red
            y_axis_config={"color": BLUE, "include_numbers": True},  # Set y-axis color to green
        )
        axes.scale(0.8)

        # Labels
        x_label = axes.get_x_axis_label("m",)
        y_label = axes.get_y_axis_label("KPa")
        x_label.set_color(GREEN)
        y_label.set_color(BLUE)
        x_label.next_to(axes.x_axis, DOWN)  # Position label below x-axis
        y_label.next_to(axes.y_axis, LEFT)  # Position label to the left of y-axis

        # Plot observed data points
        observed_dots = VGroup(*[
            Dot(axes.coords_to_point(x, y / 1000), color=RED)
            for x, y in zip(altitudes, pressures)
        ])

        # Plot fitted curve
        fitted_curve = axes.plot_line_graph(
            x_values=altitudes_fine,
            y_values=pressures_fitted / 1000,
            line_color=WHITE,
            add_vertex_dots=False,
        )

        # Create a highlight dot for pressure at 5 km
        highlight_dot = Dot(color=BLUE, radius=0.1, fill_opacity=0.75).move_to(axes.c2p(5000, pressure_at_5km / 1000))

        # Create an arrow pointing to the 5 km dot
        arrow = Arrow(
            start=axes.c2p(4500, pressures_fitted[4] / 1000),  # Start point (slightly to the left of 5 km)
            end=highlight_dot.get_center(),
            color=BLUE,
            buff=0.1,
        )

        # Create a label for pressure at 5 km, positioned above the arrow
        pressure_label = Text(f"P(5 km) = {pressure_at_5km / 1000:.2f} KPa", font_size=22).next_to(arrow, UP, buff=0.1)
        pressure_label.set_color(WHITE)

        title1 = Text("Exponential Regression Model (based on U.S. Standard Atmosphere Model):", font_size=24).to_edge(UP)
        title1.scale(0.8)

        title2 = Text("Air Pressure vs Altitude (Troposphere)", font_size=24).next_to(title1, DOWN, buff=0.3)
        title2[0:11].set_color(BLUE)  # "Air Pressure"
        title2[13:21].set_color(GREEN)  # "Altitude"

        formula = MathTex(r"P = P_0 \cdot e^{-kh}", font_size=30).next_to(title2, DOWN, buff=0.3)

        # Animate the plot
        self.play(Write(title1), run_time=2)
        self.play(Write(title2), run_time=2)
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=2)
        self.play(Create(observed_dots), run_time=2)
        self.play(Create(fitted_curve), run_time=2.5)
        self.play(Write(formula))
        self.wait(1)
        self.play(Create(arrow), FadeIn(highlight_dot), Write(pressure_label), run_time=2)
        self.wait(2)
