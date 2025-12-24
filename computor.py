import sys
from typing import TypedDict
from polynomial import Parts_linkedList
from parsing import get_coefficients, parse_equation
from solvers import solve_equation


if __name__ == "__main__":
    try:
        # if len(sys.argv) > 1:
        #     equation = sys.argv[1]
        # else:
        #     print("Error: No equation was given waiting in the STDIN")
        #     equation = input()

        equation = "-5 * X^2 = 0"

        parts_list = Parts_linkedList()

        if "=" in equation:
            left_eq, right_eq = equation.split("=")
        else:
            raise ValueError("No '=' found. Invalid Equation")
        
        parse_equation(left_eq, 1, parts_list)
    
        # Apparently the right_eq could be just 0 not 0 * X^p
        if not right_eq == ' 0':
            parse_equation(right_eq, -1, parts_list)

        print("Reduced form:", parts_list)        

        parts_list.calculate_degree()

        if parts_list.degree > 2:
            print("Polynomial degree:", parts_list.degree)
            print("The polynomial degree is strictly greater than 2, I can't solve.\n")
            exit(0)

        # Cals Section
        a, b, c = get_coefficients(parts_list)
        solve_equation(a, b, c)

    except Exception as e:
        print(f"Error: {e}")


#todolist:
# make test to run for 2 degree eq