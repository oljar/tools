import functools
import time
import math

def do_twice(func):
    @functools.wraps(func)
    def wrapper_do_twice(*args,**kwargs):
        func(*args,**kwargs)
        return func(*args,**kwargs)
    return wrapper_do_twice

def decorator(func):
     @functools.wraps(func)
     def wrapper_decorator(*args,**kwargs):
         #Do somthig before
         value = func(*args, **kwargs)
         return value
     return wrapper_decorator


def timer(func):
    """Print the runtime of the decoratetded function """
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        # Do somthig before
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        # Do something ater
        end_time = time.perf_counter()
        run_time = end_time-start_time
        print( f"finished {func.__name__!r}in{run_time:.4f}secs")
        return value
    return wrapper_timer


def debug(func):
    """Print the function signature and return vale"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        # Do somthig before
        args_repr = [repr(a) for a in args] #1
        kwargs_repr = [f"{k}={v!r}" for k,v in kwargs.items()]  #2
        signature = ", ".join(args_repr + kwargs_repr) #3
        print (f"Calling { func.__name__} {signature}")
        value = func(*args, **kwargs)
        print (f"{func.__name__!r} returned {value!r}") #4

        return value

    return wrapper_debug




