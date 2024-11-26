# Quadratic Solver

This Python project helps you solve quadratic equations of the form:

$$
ax^2 + bx + c = 0
$$

---

## Updates in This Version

- Handles **complex roots** when the discriminant is negative.
- Improved **input validation**:
  - Coefficient `a` cannot be zero.
  - Catches invalid (non-numeric) inputs.
- Clearly distinguishes between:
  - Two real roots.
  - One real root (when discriminant = 0).
  - Two complex roots.

---

## How It Works
The program calculates the roots of a quadratic equation using the quadratic formula:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

### Cases:
1. **Two real roots**: When the discriminant (\(b^2 - 4ac\)) is positive.
2. **One real root**: When the discriminant is zero.
3. **Two complex roots**: When the discriminant is negative.

It takes the coefficients `a`, `b`, and `c` as input and calculates the appropriate solutions based on these cases.

---

## Files
- **`quadratic_solver.py`**: Contains the logic for solving quadratic equations and handling user input.

---

## How to Run

1. Make sure you have Python installed on your computer.
2. Open a terminal or command prompt.
3. Run the script with the following command:

   ```bash
   python quadratic_solver.py
   ```

4. Enter the coefficients `a`, `b`, and `c` when prompted.

---

## Example Usage

### Example 1: Two Real Roots
```bash
$ python quadratic_solver.py
Quadratic Equation Solver
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots are 2.0 and 1.0
```

### Example 2: One Real Root
```bash
$ python quadratic_solver.py
Quadratic Equation Solver
Enter coefficient a: 1
Enter coefficient b: -2
Enter coefficient c: 1
There is one real root: 1.0
```

### Example 3: Complex Roots
```bash
$ python quadratic_solver.py
Quadratic Equation Solver
Enter coefficient a: 1
Enter coefficient b: 2
Enter coefficient c: 5
The roots are (-1+2j) and (-1-2j)
```

### Example 4: Invalid Input
```bash
$ python quadratic_solver.py
Quadratic Equation Solver
Enter coefficient a: 0
Coefficient a cannot be zero.
```

---

## Features
- **Handles all cases**:
  - Two real roots.
  - One real root.
  - Two complex roots.
- **Input validation**: Ensures coefficients are valid numbers and prevents division by zero.
- Interactive command-line interface for simplicity.

---

## Limitations
- Does not support non-quadratic equations (e.g., if \(a = 0\), it exits with an error).
- Outputs solutions as Python complex numbers for complex roots.

---

## Future Improvements
- Enhance user experience for complex roots (formatting the output in a more user-friendly way).
- Add a graphical user interface (GUI) for easier use.
- Support additional equation types (e.g., linear equations when \(a = 0\)).

---

### License
Free to use, modify, or share this project. Contributions are welcome! 😊
