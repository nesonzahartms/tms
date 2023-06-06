import time

def func_time(function):
    def wrapped(*args):
        start_time = time.perf_counter_ns()
        res = function(*args)
        print(time.perf_counter_ns() - start_time)
        return res
    return wrapped

@func_time
def func(first, second):
    return bin(int(first, 2) + int(second, 2))


print(func("111", "0000"))