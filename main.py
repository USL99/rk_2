import math


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
        real = -b / (2 * a)
        imaginary = math.sqrt(-d) / (2 * a)
        sol1 = complex(real, imaginary)
        sol2 = complex(real, -imaginary)
        return sol1, sol2


def main():
    print("Quadratic Equation Solver")
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

    if isinstance(roots[0], complex):
        print(f"The roots are {roots[0]} and {roots[1]}")
    elif roots[0] == roots[1]:
        print(f"There is one real root: {roots[0]}")
    else:
        print(f"The roots are {roots[0]} and {roots[1]}")


if __name__ == "__main__":
    main()
