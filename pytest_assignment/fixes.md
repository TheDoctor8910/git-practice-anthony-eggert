# Program Fixes
The following is a list of identified fixes:

1. divide_numbers: added if statement to raise a ZeroDivisionError if b = 0
2. reverse_string: added type check on s to ensure the provided value is a string
3. get_list_element: added 0 <= index check before attempting to return the list element
4. get_list_element: changed `return "Not found"` to raise an IndexError instead