# Countdown 
def countdown(number):
    list = []
    for i in range(number, -1, -1):
        list.append(i)
    return list
print(countdown(5))

# Print and Return
def print_and_return(prints, ret):
    print(prints)
    return ret
print(print_and_return('I am printed inside the function', 'I am returned from the function and printed outside'))

# First Plus Length
def first_plus_length(list):
    return len(list)+list[0]
print(first_plus_length(countdown(5)))

# Values greater than second 
def values_greater_than_second(list):
    if len(list) < 2:
        return False
    anchor = list[1]
    new_list = []
    for i in range(len(list)):
        if list[i] > anchor:
            new_list.append(list[i])
    print(len(new_list))
    return new_list

print(values_greater_than_second([3]))

# This length, that value
def this_length_that_value(length, value):
    list = []
    for i in range(length):
        list.append(value)
    return list
print(this_length_that_value(4,7))
