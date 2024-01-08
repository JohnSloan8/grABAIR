from time import time

def timer(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(
            f'\nTIMER: {func.__name__!r} executed in {(1000*(t2-t1)):.2f}ms\n')
        return result
    return wrap_func
