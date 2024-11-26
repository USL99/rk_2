import math


def solve_quadratic(a, b, c):
    # Calculate the discriminant
    d = b ** 2 - 4 * a * c

    # Find two solutions
    sol1 = (-b + math.sqrt(d)) / (2 * a)
    sol2 = (-b - math.sqrt(d)) / (2 * a)

    return sol1, sol2


def main():
    print("Quadratic Equation Solver")
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    roots = solve_quadratic(a, b, c)
    print(f"The roots are {roots[0]} and {roots[1]}")


if __name__ == "__main__":
    main()
