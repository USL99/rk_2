# Quadratic Solver

This is a simple Python project that helps you solve quadratic equations of the form:

\[ ax^2 + bx + c = 0 \]

## How It Works
The program calculates the roots of a quadratic equation using the quadratic formula:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

It takes the coefficients `a`, `b`, and `c` as input from the user and calculates the two solutions (roots).

## Files
- **`quadratic_solver.py`**: Contains the code for solving quadratic equations.

## How to Run
1. Make sure you have Python installed on your computer.
2. Open a terminal or command prompt.
3. Run the script with the command:

   ```bash
   python quadratic_solver.py
   ```

4. Enter the coefficients `a`, `b`, and `c` when prompted.

## Example
Here's an example of how the program works:

```
Quadratic Equation Solver
Enter coefficient a: 1
Enter coefficient b: -3
Enter coefficient c: 2
The roots are 2.0 and 1.0
```

## Notes
- This program assumes the equation has real roots. It will throw an error if the discriminant (\( b^2 - 4ac \)) is negative, as square roots of negative numbers are not supported here.
- Future improvements could handle complex roots or include error checking for invalid inputs.
