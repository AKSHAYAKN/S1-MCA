def replace_first_char_occurrences(input_string):
    first_string = input_string[0]
    modified_string = first_string[0] +input_string[1:-1].replace(first_string,'$')
    return modified_string
string1 = "restart"
print(f"Orginal string: '{string1}'")
print(f"Modified string:'{replace_first_char_occurrences(string1)}'")
