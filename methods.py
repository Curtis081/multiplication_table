def for_loop_method():
    for i in range(1, 10):
        for j in range(1, 10):
            product = i*j
            print("{:0>2d} ".format(product), end="")
        print()


def while_loop_method():
    i = 1
    while i <= 9:
        j = 1
        while j <= 9:
            print(f"{i * j:2d}", end=" ")
            j += 1
        print()
        i += 1


def list_comprehension_method():
    multiplication_table = [
        "{:>02d} ".format(i * j) + ("\n" if j == 9 else "")
        for i in range(1, 10) for j in range(1, 10)
    ]
    print("".join(multiplication_table))


def recursive_method():
    def print_row(i, j=1):
        if j > 9:
            return
        print(f"{i * j:0>2d}", end=" ")
        print_row(i, j + 1)

    def print_multiplication_table(i=1):
        if i > 9:
            return
        print_row(i)
        print()
        print_multiplication_table(i + 1)

    print_multiplication_table()

