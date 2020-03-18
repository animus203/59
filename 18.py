# def log(message, *values):
#     if not values:
#         print(message)
#     else:
#         values_str = ', '.join(str(x) for x in values)
#         print("%s: %s" % (message, values_str))
#
#
# log('my num are',1,3,2,4)
# log('hello')


def my_generator():
    for i in range(10):
        yield i


def my_func(*args):
    print(args)


it = my_generator()
my_func(*it)

