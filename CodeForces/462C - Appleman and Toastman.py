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
