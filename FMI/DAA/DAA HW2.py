def f(x):
    if x == 0:
        return 0

    count = 1
    count_plus_1 = 0

    while x > 1:
        if x % 2 == 0:
            count += count_plus_1
        else:
            count_plus_1 += count

        x //= 2

    return count + count_plus_1


print(f(99))
print(f(13))
print(f(2))
print(f(12))
print(f(33))
