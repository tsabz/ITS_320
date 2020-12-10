# Write a Python function that will accept as input three string values from a user.
# The method will return to the user a concatenation of the string values in reverse order.
# The function is to be called from the main method.
# In the main method, prompt the user for the three strings.

def string_reverse(first, second, third):
    reverser = (first + second + third)[::-1]
    return reverser


def main():
    first = input('First string: ')
    second = input('Second string: ')
    third = input('Three string: ')
    reverse = string_reverse(first, second, third)
    # string_reverse(first, second, third)
    print('This is your sentence reversed:', reverse)


if __name__ == '__main__':
    main()
