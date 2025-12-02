# This to tell python to Interpret the | as unios type
from __future__ import annotations

import sys
from typing import TypedDict
from dataclasses import dataclass


# Linked list for the equation parts
@dataclass
class Parts:
    coefficient: float
    exponent: int
    next: "Parts" | None = None


class Parts_linkedList:
    def __init__(self) -> None:
        # Why avoid it: If you later try to access self.head.num, the editor assumes it is safe 
        # because you promised it was a Parts object. But if it is actually None, 
        # your program crashes with an AttributeError.
        # self.head: Parts = None
        self.head: Parts | None = None

    # def to_list(self) -> list[tuple[float, int]]:
    #     """Return the list contents as a Python list for easy testing."""
    #     result: list[tuple[float, int]] = []
    #     current = self.head
    #     while current is not None:
    #         result.append((current.coefficient, current.exponent))
    #         current = current.next
    #     return result

    # def is_sorted_by_exponent_desc(self) -> bool:
    #     """Check that exponents are in non‑increasing (descending) order."""
    #     current = self.head
    #     while current and current.next:
    #         if current.exponent < current.next.exponent:
    #             return False
    #         current = current.next
    #     return True

    # def debug_print(self) -> None:
    #     """Print the linked list in a readable form (for manual debugging)."""
    #     parts: list[str] = []
    #     current = self.head
    #     while current is not None:
    #         parts.append(f"{current.coefficient} * X^{current.exponent}")
    #         current = current.next
    #     if parts:
    #         print("Linked list:", " -> ".join(parts))
    #     else:
    #         print("Linked list: <empty>")

    
    def assign_term(self, coefficient, exponent):
        # if list is empty init head
        if self.head is None:
            self.head = Parts(coefficient, exponent)
            return
        
        current = self.head
        while current:
            if current.exponent == exponent:
                current.coefficient += coefficient
                return
            
            current = current.next

            # If we break mean we didn't find the same exponent
            if current is None:
                break
        
        # Now we need to find the right fit place for the exponent
        current = self.head
        while current:

            if current.exponent < exponent and self.head == current:
                self.head = Parts(coefficient, exponent, current)
                return
                
            elif current.exponent > exponent:
                if current.next:
                    # is it in Between 
                    if current.next.exponent < exponent:
                        tmp = current.next
                        current.next = Parts(coefficient, exponent, tmp)
                        return
                # the tail
                else:
                    current.next = Parts(coefficient, exponent)


            current = current.next

parts_list = Parts_linkedList()

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


def parse_equation(eq_wing: str, side_sign: int):
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
            exponent = parts[1]
            parts_list.assign_term(float(coefficient), int(exponent))

# Note that a can't be 0 (a*x^2 + b* )

    print(parts_list)


# def test_sorted_insertion() -> None:
#     """
#     Simple test to verify that assign_term keeps the list sorted
#     by exponent in descending order and merges equal exponents.
#     """
#     ll = Parts_linkedList()

#     # Insert terms in a deliberately shuffled order
#     for coef, exp in [
#         (1.0, 2),
#         (1.0, 5),
#         (1.0, 0),
#         (1.0, 3),
#         (2.0, 5),  # same exponent as an existing term, should be merged
#         (1.0, 1),
#     ]:
#         ll.assign_term(coef, exp)

#     # Check sort order: exponents must be descending
#     assert ll.is_sorted_by_exponent_desc(), "List is not sorted by exponent (descending)"

#     # Extract exponents to check exact order
#     exponents = [exp for _, exp in ll.to_list()]
#     assert exponents == [5, 3, 2, 1, 0], f"Unexpected exponent order: {exponents}"

#     # Check merging of equal exponents (5: 1.0 + 2.0 => 3.0)
#     coeffs = {exp: coef for coef, exp in ll.to_list()}
#     assert coeffs[5] == 3.0, f"Exponent 5 should have coefficient 3.0, got {coeffs[5]}"

#     print("test_sorted_insertion passed ✅")


if __name__ == "__main__":
    try:
        # if len(sys.argv) > 1:
        #     equation = sys.argv[1]
        # else:
        #     print("Error: No equation was given waiting in the STDIN")
        #     equation = input()

        equation = "5 * X^4 + 4 * X^2 - 9.3 * X^0 = 1 * X^0"

        if "=" in equation:
            left_eq, right_eq = equation.split("=")
        else:
            raise ValueError("No '=' found. Invalid Equation")
        
        parse_equation(left_eq, 1)
        parse_equation(right_eq, -1)
        
        # left_eq = 
        # right_eq = 

    except Exception as e:
        print(f"Error: {e}")


# add a test checker from gimini