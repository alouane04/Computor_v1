def get_gcd(a, b):
    # Euclidean algorithm to find Greatest Common Divisor
    while b:
        a, b = b, a % b
    return abs(a)


def format_fraction(numerator: int | float, denominator: int | float):
    # 1. Handle Floats (e.g., 0.5 / 1.0)
    # If inputs are floats, multiply both by 10 until they are integers
    while not (numerator.is_integer() and denominator.is_integer()):
        numerator *= 10
        denominator *= 10
    
    num = int(numerator)
    den = int(denominator)

    # 2. Simplify using GCD
    common = get_gcd(num, den)
    num //= common
    den //= common

    # 3. Handle Signs (Keep negative on top)
    if den < 0:
        num = -num
        den = -den

    # 4. "If it's interesting" logic
    # If denominator is 1, it's just a normal number (e.g., 4/1 = 4)
    if den == 1:
        return f"{num}"
    else:
        return f"{num}/{den}"


def linear_equation(b, c):
    print("\n--- Step 1: Isolate the Variable ---")
    print(f"Equation: {b} * X + {c} = 0")
    print(f"Move constant to RHS: {b} * X = {-c}")

    print("\n--- Step 2: Divide by Coefficient ---")
    print(f"X = {-c} / {b}")

    # The third part
    print("The solution is:")
    # res = -c / b
    print(format_fraction(-c, b))


# def quadratic_equation(a: float, b: float, c: float) -> tuple | float | None:
def quadratic_equation(a: float, b: float, c: float):
    print("\n--- Step 1: Calculate Discriminant ---")
    print("Formula: Delta = b^2 - 4ac")
    print(f"Delta = ({b})^2 - 4 * ({a}) * ({c})")

    delta = b ** 2 - 4 * a * c

    print(f"Delta = {b**2} - {4*a*c}")
    print(f"Delta = {delta}")

    if delta > 0:
        if delta.is_integer():
            print("\n--- Step 2: Calculate Roots (Delta > 0) ---")
            print(f"sqrt(Delta) = {delta ** 0.5:.4f}")
            print("x1 = (-b - sqrt_delta) / (2a)")
            print(f"x1 = ({-b} - {delta ** 0.5:.4f}) / ({2 * a})")
            print(f"x2 = ({-b} + sqrt_delta) / (2a)")
            print(f"x2 = ({-b} + {delta ** 0.5:.4f}) / ({2 * a})")

            print(f"Discriminant is strictly positive, the two solutions are:")
            # Solution 1: (-b - sqrt) / 2a
            num1 = -b - delta ** 0.5
            den1 = 2 * a
            print(format_fraction(num1, den1))
            
            # Solution 2: (-b + sqrt) / 2a
            num2 = -b + delta ** 0.5
            den2 = 2 * a
            print(format_fraction(num2, den2))
        else:
            print("\n--- Step 2: Calculate Roots (Delta > 0) ---")
            print(f"sqrt(Delta) = {delta ** 0.5:.4f}")
            print("x1 = (-b - sqrt_delta) / (2a)")
            print(f"x1 = ({-b} - {delta ** 0.5:.4f}) / ({2 * a})")
            print(f"x2 = ({-b} + sqrt_delta) / (2a)")
            print(f"x2 = ({-b} + {delta ** 0.5:.4f}) / ({2 * a})")

            print(f"Discriminant is strictly positive, the two solutions are:")
            # we got two real solutions
            x1 = (-b + delta ** 0.5) / (2 * a)
            x2 = (-b - delta ** 0.5) / (2 * a)
            print(f"Discriminant is strictly positive, the two solutions are:\n{x2:.6f}\n{x1:.6f}")

    elif delta == 0:
        print("\n--- Step 2: Calculate one Root (Delta == 0) ---")
        print("since delta is 0 we won't need to mentioned it")

        print(f"x = ({-b} / (2a)")
        print(f"x = ({-b} / ({2 * a})")
        # we got one real solution
        # x = (-b + delta ** 0.5) / (2 * a)
        num = -b
        den = 2 * a
        print(f"Discriminant is zero, The solution is:")
        print(format_fraction(num, den))
        # return x
    # else:
    #     x1 = (-b + delta ** 0.5) / (2 * a)
    #     x2 = (-b - delta ** 0.5) / (2 * a)
    #     # we got two complex solutions
    #     print(f"Discriminant is strictly negative, the two complex solutions are:\n{x1}\n{x2}\n")
    #     # return None
    else:
        print("\n--- Step 2: Calculate Complex Roots (Delta < 0) ---")
        print("Since Delta is negative, we have complex solutions.")
        print("Formula: x = (-b / 2a) ± (sqrt(|Delta|) / 2a) * i")

        print(f"\nReal Part: -b / 2a = {-b} / {2 * a}")
        print(f"Imaginary Part: sqrt({abs(delta)}) / 2a = {abs(delta) ** 0.5:.4f} / {2 * a}")

        real_part = -b / (2 * a)
        # print("***real_part is", real_part)
        imaginary_part = (-delta) ** 0.5 / (2 * a)
        # print("***imaginary_part is", imaginary_part)

        print(f"Discriminant is strictly negative, the two complex solutions are:")
        print(f"{real_part} + {imaginary_part}i")
        print(f"{real_part} - {imaginary_part}i")

        root1_real = real_part
        root1_imaginary = imaginary_part
        root2_real = real_part
        root2_imaginary = imaginary_part

        root1 = f"{root1_real} + {root1_imaginary}i"
        root2 = f"{root2_real} - {root2_imaginary}i"

        # print("root1 is", root1)
        # print("root2 is", root2)

def solve_equation(a: float, b: float, c: float):
    if a != 0:
        print("Polynomial degree: 2")
        quadratic_equation(a, b, c)
        pass
    elif b != 0:
        print("Polynomial degree: 1")
        linear_equation(b, c)
        pass
    else:
        if c != 0:
            print("No solution.")
        else:
            print("Any real number is a solution.")
