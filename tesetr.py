import subprocess

# --- CONFIGURATION ---
# Change this to how you run your program
# Example: COMMAND = ["./computor"]  if you have a compiled binary
COMMAND = ["python3", "computor.py"] 

# Colors for pretty printing
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"
CYAN = "\033[96m"

# The Test Suite
tests = [
    # --- MANDATORY ---
    {"name": "Identity (0=0)",      "input": "0 * X^0 = 0 * X^0"},
    {"name": "Identity (5=5)",      "input": "5 * X^0 = 5 * X^0"},
    {"name": "Contradiction",       "input": "4 * X^0 = 8 * X^0"},
    {"name": "Linear Simple",       "input": "5 * X^0 + 4 * X^1 = 4 * X^0"},
    {"name": "Quadratic Real",      "input": "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"},
    {"name": "Quadratic Zero",      "input": "1 * X^0 + 2 * X^1 + 1 * X^2 = 0"},
    {"name": "Quadratic Complex",   "input": "1 * X^0 + 2 * X^1 + 5 * X^2 = 0"},
    {"name": "Degree 3",            "input": "8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0"},
    
    # --- BONUS / PARSING ---
    {"name": "Zero Coefficient",    "input": "5 * X^0 + 0 * X^2 = 5 * X^0"}, # Should be All Real Numbers or 0=0
    {"name": "Messy Spacing",       "input": "  5*X^0    =   5*X^0  "},
    {"name": "Negative Start",      "input": "-5 * X^0 = 0"},
    {"name": "Float Input",         "input": "2.5 * X^0 = 0"},

    # --- ERROR MANAGEMENT (Expect Failures) ---
    {"name": "Syntax Double **",    "input": "5 * X^0 ** X^2 = 0"},
    {"name": "Vocabulary 'Y'",      "input": "5 * Y^0 = 0"},
    {"name": "Bad Float",           "input": "5.2.2 * X^0 = 0"},
    {"name": "Empty Input",         "input": ""}
]

def run_tests():
    print(f"{CYAN}Starting ComputorV1 Automated Tests...{RESET}\n")

    for test in tests:
        print(f"{CYAN}[TEST] {test['name']}{RESET}")
        print(f"Input: \"{test['input']}\"")
        
        try:
            # Run the command with the input argument
            result = subprocess.run(
                COMMAND + [test['input']], 
                capture_output=True, 
                text=True, 
                timeout=2
            )
            
            # Print STDOUT (Standard Output)
            if result.stdout:
                print(f"{GREEN}Output:{RESET}\n{result.stdout.strip()}")
            
            # Print STDERR (Standard Error) - Good for Bonus Error Messages
            if result.stderr:
                print(f"{RED}Error Output:{RESET}\n{result.stderr.strip()}")

            # Check return code
            if result.returncode != 0:
                print(f"{RED}Exited with status: {result.returncode}{RESET}")
            else:
                print(f"{GREEN}Exited Successfully (0){RESET}")

        except Exception as e:
            print(f"{RED}CRASHED OR FAILED TO RUN: {e}{RESET}")
        
        print("-" * 50)

if __name__ == "__main__":
    run_tests()