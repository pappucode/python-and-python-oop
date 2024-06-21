def outer_func():
    message = 'Hi'

    def inner_func():
        print(message)  #Here message is a free variable
    return inner_func

my_func = outer_func()
print(my_func.__name__)
my_func()
my_func()
my_func()


# def outer_func(msg):
#     message = msg

#     def inner_func():
#         print(message)  #Here message is a free variable
#     return inner_func

# hi_func = outer_func("Hi")
# hello_func = outer_func("Hello")
# hi_func()
# hello_func()


## Without modification of Global variable

# create a Global variable
# message = "Hi, Global!"
# def outer_func():
#     def inner_func():
#         print(message)
#     return inner_func

# # Create a closure
# my_closure = outer_func()
# my_closure()
# print(my_closure.__name__)


## With modification of Global variable
# create a global variable
# counter = 0
# def outer_func():
#     def inner_func():
#         global counter
#         counter += 1
#         return counter
#     return inner_func

# # create a closure
# my_closure = outer_func()

# # call the closure multiple times
# print(my_closure())
# print(my_closure())

# # direct access to the global variable
# print(counter)
