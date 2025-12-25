import re
import sys
from typing import TypedDict
from polynomial import Parts_linkedList
from parsing import get_coefficients, parse_equation
from solvers import solve_equation


def check_syntax(equation_str):
    # Check for empty equals (nothing on one side)
    if equation_str.startswith("=") or equation_str.endswith("="):
        raise ValueError("Syntax Error: Equation cannot start or end with '='.")
    
    # Check for double operators (simple check)
    bad_sequences = ["**", "^^", "++", "--", "..", "^*", "*^"]
    for bad in bad_sequences:
        if bad in equation_str:
            raise ValueError(f"Syntax Error: Invalid sequence '{bad}' found.")


def check_vocabulary(equation_str):
    # Allow: digits, space, dot, +, -, *, =, ^, X, x
    # The pattern ^[...]+$ means "Start to End, only these chars allowed"
    allowed_pattern = r"^[0-9xX\+\-\*\^=\.\s]+$"
    
    if not re.match(allowed_pattern, equation_str):
        print("Error: Input contains invalid characters (Vocabulary Error).")
        sys.exit(0)


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            equation = sys.argv[1]
        else:
            print("No equation was given waiting in the STDIN")
            equation = input()

        # equation = "2 * X^2 + 5 * X + 2 = 0"

        check_syntax(equation)
        check_vocabulary(equation)

        parts_list = Parts_linkedList()

        if "=" in equation:
            left_eq, right_eq = equation.split("=")
        else:
            raise ValueError("No '=' found. Invalid Equation")

        parse_equation(left_eq, 1, parts_list)
    
        # Apparently the right_eq could be just 0 not 0 * X^p
        if not right_eq.replace(" ", "") == '0':
            parse_equation(right_eq, -1, parts_list)

        print("Reduced form:", parts_list)        

        parts_list.calculate_degree()

        if parts_list.degree > 2:
            print("Polynomial degree:", parts_list.degree)
            print("The polynomial degree is strictly greater than 2, I can't solve.\n")
            sys.exit(0)

        # Cals Section
        a, b, c = get_coefficients(parts_list)
        solve_equation(a, b, c)

    except Exception as e:
        error_msg = str(e)
        # if about convertion error
        if "could not convert string to float:" in error_msg:
            # deep checking the problem
            bad_input = error_msg.split(":")[-1].strip()

            if "*" in bad_input:
                print(f"Syntax Error: You likely have a double operator (like '**') near '{bad_input}'.")
            else:
                print(f"Syntax Error: '{bad_input}' is not a valid number.")
        elif "too many values to unpack" in error_msg:
            print("Syntax Error: You likely have a double operator (like '==')")
        else:
            print(f"Error: {e}")


#todolist:
# make test to run for 2 degree eq