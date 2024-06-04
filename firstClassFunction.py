def square(x):
    return x * x

f = square(5)
print(square)
print(f)

# f = square
# print(square)
# print(f)

# f = square
# print(square)
# print(f(5))



# def cube(x):
#     return x * x * x


# def my_map(func, arg_list):
#     result = []
#     for i in arg_list:
#         result.append(func(i))
#     return result

# squares = my_map(cube, [1,2,3,4,5])
# print(squares)

# def logger(msg):

#     def log_message():
#         print("Log: ", msg)
#     return log_message

# log_hi = logger("Hi!")
# log_hi()