# Appleman and Toastman play a game. Initially Appleman gives one group of n numbers to the Toastman,
#  then they start to complete the following tasks:
#
# - Each time Toastman gets a group of numbers, he sums up all the numbers and adds this sum to the score.
# Then he gives the group to the Appleman.
#
# - Each time Appleman gets a group consisting of a single number, he throws this group out.
# Each time Appleman gets a group consisting of more than one number, he splits the group into two non-empty groups
# (he can do it in any way) and gives each of them to Toastman.
#
# After guys complete all the tasks they look at the score value.
# What is the maximum possible value of score they can get?
#
# Input
# The first line contains a single integer n (1 ≤ n ≤ 3x10^5). 
# The second line contains n integers a1, a2, ..., an (1 ≤ ai ≤ 10^6) — the initial group that is given to Toastman.
#
# Output
# Print a single integer — the largest possible score.
#


def read():
    n = int(input())

    nums = [int(x) for x in input().split(' ')]

    return nums


def solve_naive(numbers):
    def appleman(arr):
        if len(arr) == 1:
            return 0

        first, second = split(arr)

        return toastman(first) + toastman(second)

    def toastman(arr):
        s = sum(arr)

        return s + appleman(arr)

    def sort_split_first(arr):
        arr.sort()

        return arr[:1], arr[1:]

    split = sort_split_first

    return toastman(numbers)


def solve_dyn(arr):
    arr.sort(reverse=True)

    dyn = [0] * (len(arr) + 1)
    sums = [0] * (len(arr) + 1)

    dyn[1] = arr[0]
    sums[1] = arr[0]

    for i in range(2, len(arr) + 1):
        sums[i] = sums[i - 1] + arr[i - 1]
        dyn[i] = dyn[i - 1] + sums[i] + arr[i - 1]

    return dyn[len(arr)]


# print(solve_naive(read())) Slow and memory inefficient
print(solve_dyn(read()))
