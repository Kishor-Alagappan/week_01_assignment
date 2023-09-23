def string_manipulator(user_input):
    # Reverse the string 
    r_string  = user_input[::-1]

    # Converts every alternate character to uppercase in the reverse string 
    new_list = []
    for index, item in enumerate(r_string):
        if index % 2 == 1 :
            item = item.upper()
        new_list.append(item)
    # Returns the manipulated string. 
    manipulated_string = ''.join(new_list)
    return manipulated_string

user_input = input('Enter the String: ')
print(string_manipulator(user_input))


