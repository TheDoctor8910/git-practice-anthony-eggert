def divide_numbers(a, b):
    """Returns the result of a divided by b, rounded to two decimals."""
    if b == 0:
        raise ZeroDivisionError("Cannot divide a number by zero")
    result = a / b  # Bug: No handling for division by zero
    return round(result, 2)


def reverse_string(s):
    """Returns the reversed string, with each character's case flipped."""
    if not isinstance(s, str):
        raise TypeError("reverse_string only supports string arguments")
    reversed_s = s[::-1]  # Bug: Might not handle non-string input properly
    flipped_case = ''.join([char.swapcase() for char in reversed_s])
    return flipped_case


def get_list_element(lst, index):
    """Returns the element at the given index in the list, or 'Not found' if out of range."""
    if 0 <= index < len(lst):  # Bug: Incorrect boundary check
        return lst[index]
    else:
        raise IndexError("Selected index outside list boundaries")