# Quadratic Solver with Visualization

This Python project helps you solve quadratic equations of the form:

$$
ax^2 + bx + c = 0
$$

In addition to solving the equation, the program visualizes the quadratic function on a graph and marks the roots. If the roots are real, they will be shown as points on the x-axis; if the roots are complex, the graph will show no intersections with the x-axis.

---

## Features
- **Solves quadratic equations**: Handles real and complex roots.
- **Graphical visualization**: Plots the quadratic equation and marks the roots on the graph.
- **Graph image saving**: Saves the graph as an image file (`quadratic_graph.png`).
- **Input validation**: Ensures valid numeric inputs and handles cases where the coefficient `a` is zero.

---

## How It Works

The program calculates the roots of a quadratic equation using the quadratic formula:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Cases:
1. **Two real roots**: When the discriminant (\(b^2 - 4ac\)) is positive.
2. **One real root**: When the discriminant is zero.
3. **Complex roots**: When the discriminant is negative.

After calculating the roots, the program plots the quadratic function \(y = ax^2 + bx + c\) and displays the roots on the graph (if real). The graph is saved as an image file for later use.

---

## Files
- **`quadratic_solver.py`**: Contains the code for solving the quadratic equation, plotting the graph, and handling user input.
- **`quadratic_graph.png`**: The image file where the graph is saved.

---

## Requirements

- Python 3.x
- **Matplotlib** and **NumPy** libraries:
   Install the required libraries using pip:
   ```bash
   pip install matplotlib numpy
   ```

---

## How to Run

1. Clone or download the repository.
2. Open a terminal or command prompt.
3. Run the script:
   ```bash
   python quadratic_solver.py
   ```
4. Enter the coefficients `a`, `b`, and `c` when prompted.

---

## Example Usage

### Example 1: Two Real Roots
```bash
$ python quadratic_solver.py
Quadratic Equation Solver with Visualization
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots are 2.0 and 1.0
Graph saved as 'quadratic_graph.png'.
```

### Example 2: One Real Root
```bash
$ python quadratic_solver.py
Quadratic Equation Solver with Visualization
Enter coefficient a: 1
Enter coefficient b: -2
Enter coefficient c: 1
There is one real root: 1.0
Graph saved as 'quadratic_graph.png'.
```

### Example 3: Complex Roots
```bash
$ python quadratic_solver.py
Quadratic Equation Solver with Visualization
Enter coefficient a: 1
Enter coefficient b: 2
Enter coefficient c: 5
The equation has complex roots.
Graph saved as 'quadratic_graph.png'.
```

### Example 4: Invalid Input
```bash
$ python quadratic_solver.py
Quadratic Equation Solver with Visualization
Enter coefficient a: 0
Coefficient a cannot be zero.
```

---

## Limitations
- The program does not handle non-quadratic equations (i.e., when \(a = 0\)).
- Complex roots are displayed as Python complex numbers and may not be as visually informative as real roots.

---

## Future Improvements
- Add better handling for complex roots in the graph.
- Implement a graphical user interface (GUI) for easier usage.
- Support additional equation types (e.g., linear equations when \(a = 0\)).

---

### License
Free to use, modify, or share this project.