
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