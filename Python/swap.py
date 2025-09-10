def swap_first_last(s):
    if len(s) <= 1:
        return s
    return s[-1]+s[1:-1]+s[0]
input_string = "hello"
result =  swap_first_last(input_string)
print("orginal:",input_string)
print("modified:",result)
    