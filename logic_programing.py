from kanren import run, eq, membero, var, lall

x = var()
print(run(1, x, eq(x, 5)))