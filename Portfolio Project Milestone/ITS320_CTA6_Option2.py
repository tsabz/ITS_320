
def cartesian():
    # arrays that the user inputs will be appended too
    a_lst = []
    b_lst = []

    a_input = int(input("Please enter the number of elements in list a: "))

    if a_input > 10:
        print("Please enter no more than 10 numbers")
        a_input = int(input("Please enter the number of elements in list a: "))

    b_input = int(input("Please enter the number of elements in list b: "))

    if b_input > 10:
        print("Please enter no more than 10 numbers")
        b_input = int(input("Please enter the number of elements in list b: "))

    for i in range(0, a_input):
        j = int(input("Enter number for list a: "))
        a_lst.append(j)

    for k in range(0, b_input):
        l = int(input("Enter number for list b: "))
        b_lst.append(l)

    a = a_lst
    b = b_lst

    cart_list = [(i, j) for i in a for j in b]
    print(cart_list)


def main():
    cartesian()


if __name__ == '__main__':
    main()
