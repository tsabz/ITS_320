# Write a Python function that will accept as input three string values from a user.
# The method will return to the user a concatenation of the string values in reverse order.
# The function is to be called from the main method.
# In the main method, prompt the user for the three strings.

def string_reverse(first, second, third):
    return first + second + third


def main():
    first = input('First string: ')[::-1]
    second = input('Second string: ')[::-1]
    third = input('Three string: ')[::-1]
    reverse = string_reverse(first, second, third)
    # string_reverse(first, second, third)
    print('This is your sentence reversed:', reverse)


if __name__ == '__main__':
    main()
