from polynomial import Parts_linkedList


# The 4 Rules of "Free Form" Normalization
# Your Normalizer needs to apply these rules in this specific order:

# Missing X: If a term is just a number (e.g., 5), turn it into 5 * X^0.

# Missing Power: If a term has X but no ^ (e.g., 4 * X or X), add ^1.

# Missing Coefficient: If a term starts with X (e.g., X^2), add 1 *.

# Implicit Multiplication: If a number sticks to X (e.g., 5X), add the *.

def normilazer(terms: list[str]):
    clean_terms: list[str] = []

    for term in terms:
        if term.isnumeric():
            clean_terms.append(term + "*X^0")
        elif term.startswith("X"):
            clean_terms.append("1*" + term)
        elif "X" in term:
            if "*" in term:
                # This to make sure that it's not already have the ^1
                if term.split("*")[1] == "X":
                    clean_terms.append(term + "^1")
                # In case the term is good and right format already
                else:
                    clean_terms.append(term)

            else:
                if term == "X":
                    clean_terms.append(term + "^1")
        elif term.endswith("X") and term[0].isdigit():
            parts = term.split("X")
            clean_terms.append(parts[0] + "*X")
    
    return clean_terms


def parse_equation(eq_wing: str, side_sign: int, parts_list: Parts_linkedList):
    clean_eq = eq_wing.replace(" ", "") # Remove spaces
    
    # Do the Ai trick of replacing - with +- so we can split freely on +
    clean_eq = clean_eq.replace("-", "+-")

    if clean_eq.startswith("+-"):
    #     # The line `clean_eq = clean_eq[1:]` is removing the first character from the string
    #     # `clean_eq`. This is done to handle the case where the equation starts with "+-" after the
    #     # initial cleaning steps. By removing the first character, it ensures that the equation is
    #     # properly formatted for further processing without the leading "+-".
        clean_eq = clean_eq[1:]

    terms = clean_eq.split("+")

    terms = normilazer(terms)
    
    for term in terms:
        if "*X^" in term:

            parts = term.split("*X^")
            # Check if we actually got 2 parts
            if len(parts) != 2:
                raise ValueError(f"Malformed term: {term}")

            coefficient = float(parts[0]) * side_sign
            if parts[1] == '':
                raise ValueError(f"Unsupported term format: '{term}'")

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
