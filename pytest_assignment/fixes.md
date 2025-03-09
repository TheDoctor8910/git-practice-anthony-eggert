# Program Fixes
The following is a list of identified fixes:

1. divide_numbers
    - bug: no handling division by zero
    - added if statement to raise a ZeroDivisionError if b = 0
2. reverse_string
    - bug: problematic behavior if input is not a string
    - added type check on s to ensure the provided value is a string
3. get_list_element
    - bug: improper boundary check for index
    - added 0 <= index check before attempting to return the list element
4. get_list_element
    - bug: returns "Not found" when the index is out-of-bounds
    - changed `return "Not found"` to raise an IndexError instead