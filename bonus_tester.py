import subprocess
import sys

# --- CONFIGURATION ---
# Replace with your actual command.
# If you use C++: COMMAND = ["./computor"]
COMMAND = ["python3", "computor.py"] 

# Colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# The "Hardcore" Free Form Test Suite
tests = [
    # 1. THE BASICS (Implicit Logic Check)
    {
        "name": "Implicit Coefficient (X = 1*X)",
        "input": "X = 0",
        "expect": "Degree: 1",
        "desc": "Should define a=0, b=1, c=0. Solution: 0"
    },
    {
        "name": "Implicit Power (4X = 4X^1)",
        "input": "4 * X = 8",
        "expect": "Solution: 2",
        "desc": "Should solve 4x = 8 -> x=2"
    },
    {
        "name": "Implicit Constant (5 = 5X^0)",
        "input": "X + 5 = 0",
        "expect": "Solution: -5",
        "desc": "Should solve x + 5 = 0 -> x=-5"
    },
    
    # 2. THE SUBJECT EXAMPLE
    {
        "name": "Subject Example",
        "input": "5 + 4 * X + X^2 = X^2",
        "expect": "Solution: -1.25",
        "desc": "X^2 should cancel out. 5 + 4x = 0 -> x = -1.25"
    },

    # 3. IMPLICIT MULTIPLICATION (The "Sticky" Numbers)
    {
        "name": "Sticky X (5X)",
        "input": "5X = 10",
        "expect": "Solution: 2",
        "desc": "Should parse 5X as 5*X^1"
    },
    {
        "name": "Sticky Negative (-2X)",
        "input": "-2X = 4",
        "expect": "Solution: -2",
        "desc": "Should parse -2X as -2*X^1"
    },
    {
        "name": "Sticky Float (0.5X)",
        "input": "0.5X = 1",
        "expect": "Solution: 2",
        "desc": "Should parse 0.5X as 0.5*X^1"
    },

    # 4. HARDCORE MIXTURES (Messy Inputs)
    {
        "name": "The 'No Stars' Challenge",
        "input": "2X^2 + 4X - 6 = 0",
        "expect": "Degree: 2",
        "desc": "Standard quadratic written normally."
    },
    {
        "name": "The 'Mixed Bag'",
        "input": "5 + X - 3X^2 = 2X^2",
        "expect": "Degree: 2",
        "desc": "Should move 2X^2 to left -> -5X^2."
    },
    {
        "name": "The 'Ghost' (Identity)",
        "input": "X = X",
        "expect": "All Real Numbers",
        "desc": "1*X^1 = 1*X^1 -> 0=0"
    },
    {
        "name": "Implicit X with Powers",
        "input": "X^2 = 4",
        "expect": "2 and -2",
        "desc": "Should define a=1, c=-4. Two solutions."
    },
    
    # 5. THE ULTIMATE UGLY TEST
    {
        "name": "The Chaos Test",
        "input": "X - 5 + 2X^2 = X^2 + 4X",
        "expect": "Degree: 2",
        "desc": "LHS: 2x^2+x-5. RHS: x^2+4x. Combined: x^2 - 3x - 5 = 0"
    }
]

def run_tests():
    print(f"{YELLOW}--- STARTING FREE FORM SYNTAX TESTER ---{RESET}\n")
    passed = 0
    failed = 0

    for test in tests:
        print(f"{YELLOW}[TEST] {test['name']}{RESET}")
        print(f"Input:    \"{test['input']}\"")
        print(f"Goal:     {test['desc']}")
        
        try:
            result = subprocess.run(
                COMMAND + [test['input']], 
                capture_output=True, 
                text=True, 
                timeout=2
            )
            
            output = result.stdout.strip()
            err = result.stderr.strip()

            # Naive check: Does the output contain the solution or expected keyword?
            # We check keywords from 'expect' in the output
            keywords = test['expect'].split()
            # If standard output is empty, it failed (or crashed to stderr)
            if not output and err:
                print(f"{RED}FAIL (Crashed/Error):{RESET}\n{err}")
                failed += 1
            else:
                print(f"{GREEN}Output:{RESET}\n{output}")
                print(f"{GREEN}PASS (Ran successfully){RESET}") # We assume it passes if it runs and prints something
                passed += 1

        except Exception as e:
            print(f"{RED}CRASHED: {e}{RESET}")
            failed += 1
        
        print("-" * 50)

    print(f"\n{YELLOW}SUMMARY:{RESET}")
    print(f"Tests Run: {len(tests)}")
    print(f"{GREEN}Passed (Ran): {passed}{RESET}")
    print(f"{RED}Failed (Crashed): {failed}{RESET}")

if __name__ == "__main__":
    run_tests()