"""
Profiling 4 ways to call functions with an integer index.

Each round, a large number of random indexes are generated, calling all the
functions (including the default). The functions are shuffled each round and
called once for each of the indexes.
"""

import random
from cProfile import Profile


# fmt:off
def A()->str: return "A"
def B()->str: return "B"
def C()->str: return "C"
def D()->str: return "D" # default


def if_else(n: int) -> str:
    if n == 0:
        return A()
    elif n == 1:
        return B()
    elif n == 2:
        return C()
    else:
        return D()


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


def dict_prop(n: int) -> str:
    return dict_prop._funcs.get(n, D)()


dict_prop._funcs = {
    0: A,
    1: B,
    2: C,
}


def dict_var(n: int) -> str:
    funcs = {
        0: A,
        1: B,
        2: C,
    }
    return funcs.get(n, D)()


def main():
    funcs = [if_else, match_stmt, dict_prop, dict_var]
    for i in range(16):
        print(f"==== round {i} ====")
        nums = random.choices(range(5), k=1_000_000)
        random.shuffle(funcs)
        for f in funcs:
            print(f" {f.__name__}")
            for n in nums:
                f(n)


if __name__ == "__main__":
    p = Profile()
    p.enable()
    main()
    p.disable()
    p.dump_stats("stats.prof")
