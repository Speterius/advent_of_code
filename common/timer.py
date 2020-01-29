from functools import wraps
import time


def timer(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        start = time.time()
        res = f(*args, **kwargs)
        end = time.time()
        print(f'Function {f.__name__} took: {(end-start):.3f} seconds.')

        return res
    return wrapped
