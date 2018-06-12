# Problem
# Supervin has a unique calculator. This calculator only has a display, a plus button, and a minus button.
# Currently, the integer N is displayed on the calculator display.

# Pressing the plus button increases the current number displayed on the calculator display by 1.
# Similarly, pressing the minus button decreases the current number displayed on the calculator display by 1.
# The calculator does not display any leading zeros. For example, if 100 is displayed on the calculator display,
# pressing the minus button once will cause the calculator to display 99.

# Supervin does not like odd digits, because he thinks they are "odd".
# Therefore, he wants to display an integer with only even digits in its decimal representation, using only the calculator buttons.
# Since the calculator is a bit old and the buttons are hard to press, he wants to use a minimal number of button presses.

# Please help Supervin to determine the minimum number of button presses to make the calculator display an integer with no odd digits.

# Input
# The first line of the input gives the number of test cases, T. T test cases follow.
# Each begins with one line containing an integer N: the integer initially displayed on Supervin's calculator.

# Output
# For each test case, output one line containing Case #x: y, where:
# x is the test case number (starting from 1) and
# y is the minimum number of button presses, as described above.


def solve():
    n = int(input())

    for i in range(n):
        x = int(input())

        print('Case #' + str(i + 1) + ': ' + str(moves_arr(x)))


def moves_naive(x):
    if has_even_digits(x):
        return 0

    res = 1

    while not has_even_digits(x - res) and not has_even_digits(x + res):
        res += 1  # Can be optimized to add 2 if x is even

    return res


def has_even_digits(x):
    while x > 0:
        if x % 2 != 0:
            return False

        x //= 10

    return True


def moves_arr(x):
    smaller = [int(n) for n in str(x)]
    bigger = [int(n) for n in str(x)]

    for i in range(len(smaller)):
        if smaller[i] % 2 != 0:
            smaller[i] -= 1

            if bigger[i] == 9 and i >= 1:
                bigger[i] = 0
                bigger[i - 1] = bigger[i - 1] + 2
            elif bigger[i] == 9:
                bigger[i] = 22
            else:
                bigger[i] = bigger[i] + 1

            for u in range(i + 1, len(smaller)):
                smaller[u] = 8
                bigger[u] = 0

            break

    smaller = ''.join(map(str, smaller))
    bigger = ''.join(map(str, bigger))

    return min(abs(int(smaller) - x), abs(int(bigger) - x))


solve()
