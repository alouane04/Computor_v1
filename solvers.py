from math import sqrt


def linear_equation(b, c):
    print("The solution is:")
    res = -c / b
    print(res, "\n")


# def quadratic_equation(a: float, b: float, c: float) -> tuple | float | None:
def quadratic_equation(a: float, b: float, c: float):
    delta = b ** 2 - 4 * a * c

    if delta > 0:
        # we got two real solutions
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Discriminant is strictly positive, the two solutions are:\n{x2:.6f}\n{x1:.6f}\n")
        # return x1, x2
    elif delta == 0:
        # we got one real solution
        x = (-b + delta ** 0.5) / (2 * a)
        print(f"The solution is:\n{x}\n")
        # return x
    # else:
    #     x1 = (-b + delta ** 0.5) / (2 * a)
    #     x2 = (-b - delta ** 0.5) / (2 * a)
    #     # we got two complex solutions
    #     print(f"Discriminant is strictly negative, the two complex solutions are:\n{x1}\n{x2}\n")
    #     # return None
    else:
        real_part = -b / (2 * a)
        # print("***real_part is", real_part)
        imaginary_part = (-delta) ** 0.5 / (2 * a)
        # print("***imaginary_part is", imaginary_part)

        print(f"Discriminant is strictly negative, the two complex solutions are:")
        print(f"{real_part} + {imaginary_part}i")
        print(f"{real_part} - {imaginary_part}i\n")

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
            print("No solution.\n")
        else:
            print("Any real number is a solution.\n")
