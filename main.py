import random
import traceback
import tracemalloc
from contextlib import contextmanager
from cProfile import Profile
from typing import Any, Generator, final


# fmt:off
def A()->str: return "A"
def B()->str: return "B"
def C()->str: return "C"
def D()->str: return "D"
# fmt:on


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


snapshots: dict[str, list[tracemalloc.StatisticDiff]] = {}


@contextmanager
def trace(name: str) -> Generator[None, None, None]:
    before = tracemalloc.take_snapshot()
    try:
        yield
    finally:
        after = tracemalloc.take_snapshot()
        snapshots[name] = after.compare_to(before, "lineno")


def print_snapshots():
    for name, stats in snapshots.items():
        print()
        print(name)
        stats = [s for s in stats if "main.py" in str(s.traceback)]
        for line in stats:
            print(line)


def main():
    # tracemalloc.start()

    funcs = [if_else, match_stmt, dict_prop, dict_var]
    nums = random.choices(range(5), k=500_000)
    for i in range(16):
        print(f"-- round {i} --")
        random.shuffle(funcs)
        for f in funcs:
            print(f.__name__)
            for n in nums:
                f(n)

    # for f in (if_else, match_stmt, dict_prop, dict_var):
    #     # with trace(f.__name__):
    #     before = tracemalloc.take_snapshot()
    #     f(1)
    #     after = tracemalloc.take_snapshot()
    #     snapshots[f.__name__] = after.compare_to(before, "lineno")

    # print_snapshots()


if __name__ == "__main__":
    p = Profile()
    p.enable()
    main()
    p.disable()
    p.dump_stats("stats.prof")
