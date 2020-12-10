# write a function that will accept 3 string values from a user   # 3 string values as params

# method will return to the user a concatenation of the first two string and will print the third string in reverse order

# in the main method prompt the user for the three strings
def third_string_reverse(first, second, third):
    return first + second + third


def main():
    first = input('First string: ')
    second = input('Second string: ')
    third = input('Three string: ')[::-1]
    first_second_driht = third_string_reverse(first, second, third)

    # third_string_reverse(first, second, third)
    print('First and second:', first_second_driht)


if __name__ == '__main__':
    main()
