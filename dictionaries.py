# def main():
#     animals = {
#         'Kitten': 'meow',
#         'Puppy': 'ruff!',
#         'Lion': 'grrr'
#     }
#     for k, v in animals.items():
#         # print(f'{k}: {v}')
#         print(k)


# if __name__ == '__main__':
#     main()

# Contacts = {
#     id: 1,  # int
#     'First_Name': 'Tonia',  # string
#     'Last_Name': 'Saba',
#     'Birthday': '09/14/1993',  # string
#     'Address':  '333 3rd st bronx NYC'  # string
# }

# print(Contacts)

conact_dict = {'Mike Meyers': {'First Name': 'Michael',
                               'Last Name': 'Meyers',
                               'DOB': '19630525',
                               'Address of Extended Family': '123 Yeah Baby Yea St Liverpool UK'},
               'Dana Carvey': {'First Name': 'Dana',
                               'Last Name': 'Carvey',
                               'DOB': '19550602',
                               'Address of Extended Family': '456 Turtle St Chicago IL', }}


conact_dict['Tonia Saba'] = {'First Name': 'Tonia',
                             'Last Name': 'Saba',
                             'DOB': '19630525',
                             'Address of Extended Family': '123 Yeah Baby Yea St Liverpool UK'}

for a in conact_dict:
    print(a, ':', conact_dict[a])

# print('This is Mike: ', conact_dict['Mike Meyers'])


# contact_dict = dict()

# contact_dict['Mike Meyers'] = {
#     'First Name': 'Michael',
#     'Last Name': 'Meyers',
#     'DOB': '19630525',
#     'Address of Extended Family': '123 Yeah Baby Yea St Liverpool UK',
# }
# contact_dict['Dana Carvey'] = {
#     'First Name': 'Dana',
#     'Last Name': 'Carvey',
#     'DOB': '19550602',
#     'Address of Extended Family': '456 Turtle St Chicago IL',
# }
# for a in contact_dict:
#     print(a, ' : ', contact_dict[a])
