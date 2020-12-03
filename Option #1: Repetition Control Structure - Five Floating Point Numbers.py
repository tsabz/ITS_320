values_dict = {
    'Module 1': 0,
    'Module 2': 0,
    'Module 3': 0,
    'Module 4': 0,
    'Module 5': 0,
}

# first we want to have the student enter grades into set


def Enter_grades():
    print('Please enter your grade for Module 1:')
    values_dict['Module 1'] = int(input())
    print('Please enter your grade for Module 2:')
    values_dict['Module 2'] = int(input())
    print('Please enter your grade for Module 3:')
    values_dict['Module 3'] = int(input())
    print('Please enter your grade for Module 4:')
    values_dict['Module 4'] = int(input())
    print('Please enter your grade for Module 5:')
    values_dict['Module 5'] = int(input())


def Average():
    avg = 0
    for value in values_dict.values():
        avg += value
    avg = avg / len(values_dict)
    print('Your average score is:')
    print(float(avg))


def min_max():
    # min numbers
    minimum = min(values_dict.values())
    print('Your minimum score was ' +
          min(values_dict) + ':')
    print(float(minimum))
    # max numbers
    maximum = max(values_dict.values())
    print('Your maximum score was ' + max(values_dict) + ':')
    print(float(maximum))


def main():
    Enter_grades()
    print(values_dict)
    Average()
    min_max()


if __name__ == "__main__":
    main()
