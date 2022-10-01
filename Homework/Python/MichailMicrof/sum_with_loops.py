""" 4521369741 → you have to find the sum of this numbers
until it's a single-digit number.
Like this : 4 + 5 + 2 + 1 + 3 + 6 + 9 + 7 + 4 + 1 = 42 > 4 + 2 = 6 (output)
 """


def sum_with_loops(test_input: int) -> int:
    total = 0
    final_total = 0
    for i in str(test_input):
        total += int(i)
    if total > 9:
        for j in str(total):
            final_total += int(j)
    return final_total


if __name__ == '__main__':
    input: int = 4521369741
    print(f'Sun {input} is {sum_with_loops(input)}')
