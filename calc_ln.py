import math

my_array = [1, 2, 3, 4, 5]

ONE = 1e6
ONE_12 = 1e12

x0 = 16000000  # 2ˆ4
a0 = 8886110520507  # eˆ(x0)
x1 = 8000000  # 2ˆ3
a1 = 2980957987  # eˆ(x1) (no decimals)
x2 = 4000000  # 2ˆ2
a2 = 54598150  # eˆ(x2)
x3 = 2000000  # 2ˆ1
a3 = 7389056  # eˆ(x3)
x4 = 1000000  # 2ˆ0
a4 = 2718281  # eˆ(x4)
x5 = 500000  # 2ˆ-1
a5 = 1648721  # eˆ(x5)
x6 = 250000  # 2ˆ-2
a6 = 1284025  # eˆ(x6)
x7 = 125000  # 2ˆ-3
a7 = 1133148  # eˆ(x7)
x8 = 62500  # 2ˆ-4
a8 = 1064494  # eˆ(x8)
x9 = 31250  # 2ˆ-5
a9 = 1031743  # eˆ(x9)
x10 = 15625  # 2ˆ-6
a10 = 1015747  # eˆ(x10)
x11 = 7812  # 2ˆ-7
a11 = 1007843  # eˆ(x11)


def calc_ln(a: int, array: list) -> int:
    # startIndex = 0  # pt.Int(0)
    left = 0  # pt.Int(0)
    arr_len = len(array)
    right = arr_len - 1  # pt.Int(arr_len) - pt.Int(1)
    mid = 0  # pt.Int(0)
    sum = 0

    while left <= right:
        mid = math.floor((left + right) / 2)
        if a >= array[mid]:
            # startIndex = mid  # pt.Int(mid)
            right = mid - 1  # pt.Int(1)
        else:
            left = mid + 1  # pt.Int(1)

    for i in range(len(array)):
        if a >= array[i]:
            a = (a * ONE) / array[i]
            sum += array[i]

    z = ((a - ONE) * ONE) / (a + ONE)
    z_squared = (z * z) / ONE
    num = z
    seriesSum = num

    num = (num * z_squared) / ONE
    seriesSum += num / 3

    num = (num * z_squared) / ONE
    seriesSum += num / 5

    num = (num * z_squared) / ONE
    seriesSum += num / 7

    num = (num * z_squared) / ONE
    seriesSum += num / 9

    num = (num * z_squared) / ONE
    seriesSum += num / 11

    seriesSum *= 2

    xxx = sum + seriesSum

    return xxx


print(calc_ln(2000000, my_array))
