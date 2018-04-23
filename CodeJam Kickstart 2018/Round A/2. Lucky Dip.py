# Problem
# You are participating in the Grand Kickstart Lucky Dip with many fantastic and amazing prizes (and some not so good ones)!

# In this Lucky Dip, there is a bag with N items. The i-th item in the bag has value Vi.
# You will put your hand into the bag and draw one item at random; all items in the bag have an equal probability of being chosen.
# The organizers want contestants to feel that they have some element of choice, so after you draw an item,
# you can either keep it, or "redip" by returning it to the bag and drawing again.
# (Note that the returned item is now just as likely to be chosen as any of the other items in the bag.)
# You may only redip a maximum of K times. If you use K redips, you must keep the item that you draw on your (K + 1)-th draw.

# If you play optimally to maximize the value of the item you will end the game with, what is the expected value of that item?

# Input
# The input starts with one line containing one integer T: the number of test cases. T test cases follow.

# Each test case consists of two lines. The first line consists of two integers N and K:
# the number of items in the bag, and the maximum number of times you may redip.
# The second line consists of N integers Vi, each representing the value of the i-th item.

# Output
# For each test case, output one line containing Case #x: y,
# where x is the test case number (starting from 1) and y is the expected value described above.
# Your answer will be considered correct if it is within an absolute or relative error of 10-6 of the correct answer.


def solve():
    n = int(input())

    for i in range(n):
        _, k = [int(x) for x in input().split()]
        nums = [int(x) for x in input().split()]

        print("Case #" + str(i + 1) + ": " + str(expected_value(nums, k)))


def expected_value(arr, redips):  # Can be optimized to run in redips * log(len(arr)) time, not redips * len(arr)
    dyn = [0] * (redips + 1)

    dyn[0] = sum(arr) / len(arr)

    for i in range(1, redips + 1):
        for j in range(len(arr)):
            dyn[i] += max(arr[j], dyn[i - 1]) / len(arr)

    return dyn[redips]


solve()
