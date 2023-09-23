def data_identifier(user_input):
    if isinstance(user_input, bool):
        return "Boolean"
    elif isinstance(user_input, float):
        return 'Float'
    elif isinstance(user_input, str):
        return 'String'
    elif isinstance(user_input, int):
        return 'Integer'
    else:
        return 'unknown / other'
# Test inputs to check the function.
print(data_identifier(5.0))
print(data_identifier(2))
print(data_identifier('Kishor')) 
print(data_identifier(True))



