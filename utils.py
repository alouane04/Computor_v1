import re
import sys


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


def check_sign(part):
    sign = True

    if part == "-":
        sign = False

    return sign

def is_sign(part):
    if part == "-" or part == "+":
        return True

def is_valid_number(num):
    try:
        float(num)
        return True # valid
    except TypeError:
        return False # Invalid user number input


def is_valid_positivr_number(num):
    return isinstance(num, int) and num >= 0


def check_for_Xsquared(p):
    if p[0] == 'X' and p[1] == '^':
        return is_valid_positivr_number(p[2])


def help_option():
    """Prints the help menu with usage, options, and examples."""
    help_text = """
COMPUTOR V1 - Polynomial Equation Solver

USAGE:
    python3 main.py "equation" | -h | -help

DESCRIPTION:
    Solves polynomial equations up to degree 2.
    It displays the reduced form, the degree, the discriminant (if applicable),
    and the solution(s).

OPTIONS:
    -h, --help      Show this help message and exit.

EXAMPLES:
    1. Standard Format:
       python3 main.py "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"

    2. Natural Syntax (Bonus):
       python3 main.py "5 + 4X + X^2 = X^2"
    """
    print(help_text)
