values_dict = {
    'Module 1': 0,
    'Module 2': 0,
    'Module 3': 0,
    'Module 4': 0,
    'Module 5': 0
}

# first we want to have the student enter grades into set


def Enter_grades():
    print('Please enter your grade for Module 1:')
    values_dict['Module 1'] = float(input())
    print('Please enter your grade for Module 2:')
    values_dict['Module 2'] = float(input())
    print('Please enter your grade for Module 3:')
    values_dict['Module 3'] = float(input())
    print('Please enter your grade for Module 4:')
    values_dict['Module 4'] = float(input())
    print('Please enter your grade for Module 5:')
    values_dict['Module 5'] = float(input())


def main():
    Enter_grades()
    print(values_dict)


if __name__ == "__main__":
    main()
