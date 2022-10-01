""" 4521369741 → you have to find the sum of this numbers
until it's a single-digit number
Like this : 4 + 5 + 2 + 1 + 3 + 6 + 9 + 7 + 4 + 1 = 42 > 4 + 2 = 6 (output)
 """


def func_sum_with_map(in_int: int) -> int:
    """ gets sum single-digit number"""
    while in_int > 9:
        in_int = sum(map(int, str(in_int)))
    return in_int


if __name__ == '__main__':
    input: int = 4521369741
    print(f'Sun {input} is {func_sum_with_map(input)}')
