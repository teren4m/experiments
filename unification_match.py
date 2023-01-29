from collections import defaultdict
from functools import partial

from unification import var
from unification.match import VarDispatcher, match
 
n = var('n')

@match(0)
def fib(n):
    return 0


@match(1)
def fib(n):
    return 1


@match(n)
def fib(n):
    return fib(n - 1) + fib(n - 2)

x = list(map(fib, [0, 1, 2, 3, 4, 5, 6, 7, 8, 0]))
print(x)