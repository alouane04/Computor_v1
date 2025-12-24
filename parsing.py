from polynomial import Parts_linkedList


def parse_equation(eq_wing: str, side_sign: int, parts_list: Parts_linkedList):
    # eq_list = eq_wing.split() # Split by white spaces to get list
    clean_eq = eq_wing.replace(" ", "") # Remove spaces
    
    # Do the Ai trick of replacing - with +- so we can split freely on +
    clean_eq = clean_eq.replace("-", "+-")

    if clean_eq.startswith("+-"):
        # The line `clean_eq = clean_eq[1:]` is removing the first character from the string
        # `clean_eq`. This is done to handle the case where the equation starts with "+-" after the
        # initial cleaning steps. By removing the first character, it ensures that the equation is
        # properly formatted for further processing without the leading "+-".
        clean_eq = clean_eq[1:]

    # part: Parts = {}

    terms = clean_eq.split("+")
    
    for term in terms:
        if "*X^" in term:
            parts = term.split("*X^")
            coefficient = float(parts[0]) * side_sign
            exponent = int(parts[1])
            parts_list.assign_term(coefficient, exponent)
        else:
            raise ValueError(f"Unsupported term format: '{term}'")

# Note that a can't be 0 (a*x^2 + b* )


def get_coefficients(poly_list: Parts_linkedList) -> tuple[float, float, float]:
    # Default values in case terms are missing (e.g., 5*X^2 - 9 means b=0)
    a = 0.0
    b = 0.0
    c = 0.0

    current = poly_list.head
    while current is not None:
        if current.exponent == 2:
            a = current.coefficient
        elif current.exponent == 1:
            b = current.coefficient
        elif current.exponent == 0:
            c = current.coefficient

        current = current.next

    return a, b, c
