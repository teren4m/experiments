
from multiprocessing import Process

def do_math_homework():
    res = 0
    for i in range(100_000_000):
        res += i
    return res

def do_physics_homework():
    res = 0
    for i in range(100_000_000):
        res += i
    return res

def do_chemistry_homework():
    res = 0
    for i in range(100_000_000):
        res += i
    return res

processlist = []

if __name__ == '__main__':
    processlist.append(Process(target=do_math_homework))
    processlist.append(Process(target=do_physics_homework))
    processlist.append(Process(target=do_chemistry_homework))
    
    for t in processlist:
        t.start()
        
    for t in processlist:
        t.join()