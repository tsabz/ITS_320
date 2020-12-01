

def isTrue(x):
    if x == 2:
        return x


def fun(i):
    print("executed")
    return i


def main():
    # fun(1)
    # print(1 or fun(1))  # due to short-circuiting, "executed" not printed
    # print(isTrue(2) and True)  # fun(1) called and "executed" printed
    # due to short-circuiting, "executed" not printed
    # print(True and isTrue(2))
    print(1 or fun(1))
    # print(5 > 6 > fun(3))
    # print(5 < 6 > fun(3))
    # print(4 <= 6 > fun(7))
    # print(5 < fun(6) < 3)
    # print(3 and 5)
    # print(2 or 5)
    # print(True or 3/0)
    # print(False or 3/0)


if __name__ == "__main__":
    main()
