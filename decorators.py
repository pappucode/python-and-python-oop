# def decorator_function(original_function):
#     def wrapper_function(*args,**kwargs):
#         print("wrapper function executed this before {}".format(original_function.__name__))
#         return original_function(*args,**kwargs)
#     return wrapper_function

# @decorator_function
# def display():
#     print('display function run')
    
# ## Actually @decorator_function doing same like the below 2 lines.    
# # display = decorator_function(display)
# # display()

# @decorator_function
# def display_info(name, age):
#     print('display_info run with arguments ({}, {})'.format(name, age))

# display_info('John', 25)
# display()

## Practical demonstration of decorator function
from functools import wraps

def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)

    return wrapper

def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result

    return wrapper

import time
@my_logger
@my_timer
def display_info(name, age):
    time.sleep(2)
    print('display_info ran with argguments ({}, {})'.format(name, age))

display_info('Pappu Akondo', age=32)



















