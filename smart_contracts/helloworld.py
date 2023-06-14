import beaker
import math
import pyteal as pt

from smart_contracts.helpers.deployment_standard import (
    deploy_time_immutability_control,
    deploy_time_permanence_control,
)

app = (
    beaker.Application("HelloWorldApp")
    .apply(deploy_time_immutability_control)
    .apply(deploy_time_permanence_control)
)


# a1 = (1, pt.abi.ByteTypeSpec)
# a2 = (2, pt.abi.ByteTypeSpec)
# a3 = (3, pt.abi.ByteTypeSpec)
# a4 = (4, pt.abi.ByteTypeSpec)
# a5 = (5, pt.abi.ByteTypeSpec)

_a1 = pt.Int(1)
_a2 = pt.Int(2)
_a3 = pt.Int(3)
_a4 = pt.Int(4)
_a5 = pt.Int(5)

my_array = (
    [_a1, _a2, _a3, _a4, _a5],
    pt.abi.StaticArrayTypeSpec,
)


ONE = pt.Int(int(1e6))
ONE_12 = pt.Int(int(1e12))

# ONE = int(1e6)

x0 = pt.Int(int(16000000))  # 2ˆ4
a0 = pt.Int(int(8886110520507))  # eˆ(x0)
x1 = pt.Int(int(8000000))  # 2ˆ3
a1 = pt.Int(int(2980957987))  # eˆ(x1) (no decimals)
x2 = pt.Int(int(4000000))  # 2ˆ2
a2 = pt.Int(int(54598150))  # eˆ(x2)
x3 = pt.Int(int(2000000))  # 2ˆ1
a3 = pt.Int(int(7389056))  # eˆ(x3)
x4 = pt.Int(int(1000000))  # 2ˆ0
a4 = pt.Int(int(2718281))  # eˆ(x4)
x5 = pt.Int(int(500000))  # 2ˆ-1
a5 = pt.Int(int(1648721))  # eˆ(x5)
x6 = pt.Int(int(250000))  # 2ˆ-2
a6 = pt.Int(int(1284025))  # eˆ(x6)
x7 = pt.Int(int(125000))  # 2ˆ-3
a7 = pt.Int(int(1133148))  # eˆ(x7)
x8 = pt.Int(int(62500))  # 2ˆ-4
a8 = pt.Int(int(1064494))  # eˆ(x8)
x9 = pt.Int(int(31250))  # 2ˆ-5
a9 = pt.Int(int(1031743))  # eˆ(x9)
x10 = pt.Int(int(15625))  # 2ˆ-6
a10 = pt.Int(int(1015747))  # eˆ(x10)
x11 = pt.Int(int(7812))  # 2ˆ-7
a11 = pt.Int(int(1007843))  # eˆ(x11)

aValues = (
    [a0, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11],
    pt.abi.StaticArrayTypeSpec,
)

xValues = (
    [x0, x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11],
    pt.abi.StaticBytesTypeSpec,
)


@app.external
def hello(name: pt.abi.String, *, output: pt.abi.Uint64) -> pt.Expr:
    # Exp
    total_sum = pt.ScratchVar(pt.TealType.uint64)
    # element = pt.ScratchVar(pt.TealType.uint64)
    # l = pt.ScratchVar(pt.TealType.uint64)
    # j = pt.ScratchVar(pt.TealType.uint64)
    total_sum_ = calc_ln(pt.Int(2000000), aValues.__getitem__(0))

    return pt.Seq(
        # total_sum.store(my_for(my_array.__getitem__(0))),
        total_sum.store(total_sum_),
        # pt.Assert(total_sum.load() == pt.Int(15)),
        output.set(total_sum.load()),
    )

    # return output.set(my_for())

    # return pt.Seq(
    #     pt.Assert(my_array.__getitem__(0)[0] == a1),
    #     total_sum.store(pt.Int(0)),
    #     l.store(pt.Int(5)),
    #     pt.For(
    #         j.store(pt.Int(0)),
    #         j.load() < l.load(),
    #         j.store(j.load() + pt.Int(1)),
    #     ).Do(
    #         # (x.set(j.load())),
    #         # total_sum.store(j.load() + pt.Int(10))
    #         pt.Assert(j.load() == pt.Int(0)),
    #         element.store(my_array.__getitem__(0)[int(j.load())]),
    #         total_sum.store(total_sum.load() + element.load()),
    #     ),
    #     pt.Assert(total_sum.load() == pt.Int(5)),
    #     output.set(total_sum.load()),
    # )
    # output.set(my_array.__getitem__(0)[0]),


def my_for(my_array):
    element = pt.Int(0)
    total_sum = pt.Int(0)
    for i in range(5):
        element = my_array[i]
        total_sum = total_sum + element
    return total_sum


def calc_ln(a, array):
    startIndex = 0  # pt.Int(0)
    left = 0  # pt.Int(0)
    arr_len = len(array)
    right = arr_len - 1  # pt.Int(arr_len) - pt.Int(1)
    mid = 0  # pt.Int(0)
    sum = pt.Int(0)

    while left <= right:
        mid = math.floor((left + right) / 2)
        if a >= array[mid]:
            startIndex = mid  # pt.Int(mid)
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
    seriesSum += num / pt.Int(3)

    num = (num * z_squared) / ONE
    seriesSum += num / pt.Int(5)

    num = (num * z_squared) / ONE
    seriesSum += num / pt.Int(7)

    num = (num * z_squared) / ONE
    seriesSum += num / pt.Int(9)

    num = (num * z_squared) / ONE
    seriesSum += num / pt.Int(11)

    seriesSum *= pt.Int(2)

    xxx = sum + seriesSum

    return xxx
