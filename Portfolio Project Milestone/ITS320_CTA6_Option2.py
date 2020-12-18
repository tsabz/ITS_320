

def cartesian():
    a_input = input("Please enter numbers: ")
    b_input = input("Please enter numbers: ")

    a = a_input.replace(" ", "")
    b = b_input.replace(" ", "")

    cart_list = [(i, j) for i in a for j in b]
    print(cart_list)


def main():
    cartesian()


if __name__ == '__main__':
    main()
