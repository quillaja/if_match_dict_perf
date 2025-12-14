from memory_profiler import profile


# fmt:off
def A()->str: return "A"
def B()->str: return "B"
def C()->str: return "C"
def D()->str: return "D"
# fmt:on


@profile
def if_else(n: int) -> str:
    if n == 0:
        return A()
    elif n == 1:
        return B()
    elif n == 2:
        return C()
    else:
        return D()


@profile
def match_stmt(n: int) -> str:
    match n:
        case 0:
            return A()
        case 1:
            return B()
        case 2:
            return C()
        case _:
            return D()


@profile
def dict_prop(n: int) -> str:
    return dict_prop._funcs.get(n, D)()


dict_prop._funcs = {
    0: A,
    1: B,
    2: C,
}


@profile
def dict_var(n: int) -> str:
    funcs = {
        0: A,
        1: B,
        2: C,
    }
    return funcs.get(n, D)()


@profile
def main():
    n = 1
    if_else(n)
    match_stmt(n)
    dict_prop(n)
    dict_var(n)

    # import random
    # nums = random.choices(range(5), k=10_000)
    # for f in (if_else, match_stmt, dict_prop, dict_var):
    #     for n in nums:
    #         f(n)


if __name__ == "__main__":
    main()
