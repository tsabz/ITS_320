year = int(input('Enter year:\n'))

value = ['$18,500', '$6,000', '$12,000', '$48,000',
         '$200,000', '$650,000', '$35,000,000', '$52,000,000']


def ferrari_value():
    if year < 1962:
        print('Was not made yet')
    elif year <= 1964:
        print('Ferrari value during year', year, 'will be', value[0])
    elif year <= 1968:
        print('Ferrari value during year', year, 'will be', value[1])
    elif year <= 1971:
        print('Ferrari value during year', year, 'will be', value[2])
    elif year <= 1975:
        print('Ferrari value during year', year, 'will be', value[3])
    elif year <= 1980:
        print('Ferrari value during year', year, 'will be', value[4])
    elif year <= 1985:
        print('Ferrari value during year', year, 'will be', value[5])
    elif year <= 2012:
        print('Ferrari value during year', year, 'will be', value[6])
    elif year <= 2014:
        print('Ferrari value during year', year, 'will be', value[7])


def main():
    ferrari_value()


if __name__ == '__main__':
    main()
