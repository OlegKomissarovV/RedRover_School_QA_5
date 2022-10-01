""" 4521369741 → you have to find the sum of this numbers
until it's a single-digit number.
Like this : 4 + 5 + 2 + 1 + 3 + 6 + 9 + 7 + 4 + 1 = 42 > 4 + 2 = 6 (output)
 """


def sum_with_recursive_or_loop(input: int) -> int:
    # loop
    """ # while (test_input > 9):
    #     test_input = sum((int(x) for x in str(test_input)))
    # return test_input """
    # recursive
    input = sum((int(x) for x in str(input)))
    return input if input <= 9 else sum_with_recursive_or_loop(input)


if __name__ == '__main__':
    input: int = 4521369741
    print(f'Sum {input} is {sum_with_recursive_or_loop(input)}')
