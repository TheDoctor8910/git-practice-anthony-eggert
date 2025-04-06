import math
import random
from functools import lru_cache

from line_profiler import profile

@lru_cache(maxsize=None)
@profile
def expensive_op(n):
    return n * (999 * 1000) // 2

@profile
def slow_func(lst):
    result = []
    for i in range(len(lst)):
        result.append(expensive_op(i))
    return result

@profile
def unused_function():
    x = 10
    y = 20
    z = x + y
    return z

@profile
def main():
    numbers = list(range(1000))
    output = slow_func(numbers)
    print("Done")


if __name__ == "__main__":
    main()
