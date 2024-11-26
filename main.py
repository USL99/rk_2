import math
import matplotlib.pyplot as plt
import numpy as np


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = b ** 2 - 4 * a * c

    if d > 0:
        # Two real solutions
        sol1 = (-b + math.sqrt(d)) / (2 * a)
        sol2 = (-b - math.sqrt(d)) / (2 * a)
        return sol1, sol2
    elif d == 0:
        # One real solution
        sol = -b / (2 * a)
        return sol, sol
    else:
        # Complex solutions
        return None, None


def plot_quadratic(a, b, c, roots):
    # Determine the vertex (critical point of the parabola)
    vertex_x = -b / (2 * a)
    vertex_y = a * vertex_x ** 2 + b * vertex_x + c

    # Determine the x range dynamically
    if roots[0] is not None:
        # Expand range based on roots
        x_min = min(roots) - 2
        x_max = max(roots) + 2
    else:
        # No real roots, use vertex as the center
        x_min = vertex_x - 5
        x_max = vertex_x + 5

    # Generate x values dynamically
    x = np.linspace(x_min, x_max, 400)
    y = a * x ** 2 + b * x + c

    # Automatically calculate y range with padding
    y_values = list(y) + [vertex_y]  # Include vertex in range calculation
    y_min, y_max = min(y_values), max(y_values)
    padding = abs(y_max - y_min) * 0.1

    # Plot the function
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f"{a}x² + {b}x + {c}")

    # Plot roots if they exist
    if roots[0] is not None:
        plt.plot(roots[0], 0, 'ro', label=f"Root 1: {roots[0]:.2f}")
        plt.plot(roots[1], 0, 'bo', label=f"Root 2: {roots[1]:.2f}")

    # Highlight the vertex
    plt.plot(vertex_x, vertex_y, 'go', label=f"Vertex: ({vertex_x:.2f}, {vertex_y:.2f})")

    # Draw horizontal and vertical reference lines
    plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
    plt.axvline(vertex_x, color='grey', linewidth=0.5, linestyle='--')

    # Add titles and labels
    plt.title("Quadratic Equation Graph")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)

    # Adjust the plot range
    plt.ylim(y_min - padding, y_max + padding)
    plt.xlim(x_min, x_max)

    # Save and show the plot
    plt.savefig("quadratic_graph_dynamic.png")
    print("Graph saved as 'quadratic_graph_dynamic.png'.")


def main():
    print("Quadratic Equation Solver with Visualization")
    try:
        a = float(input("Enter coefficient a: "))
        if a == 0:
            print("Coefficient a cannot be zero.")
            return
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
    except ValueError:
        print("Please enter valid numbers.")
        return

    roots = solve_quadratic(a, b, c)

    if roots[0] is None:
        print("The equation has complex roots.")
    elif roots[0] == roots[1]:
        print(f"There is one real root: {roots[0]}")
    else:
        print(f"The roots are {roots[0]} and {roots[1]}")

    plot_quadratic(a, b, c, roots)


if __name__ == "__main__":
    main()
