import time


def cache_decorator(function):
    lookup = {}

    def wrapper(*args):
        if args in lookup:
            return lookup[args]
        else:
            result = function(*args)
            lookup[args] = result
            return result
    return wrapper


@cache_decorator
def catalan(n):
    """A function to calculate catalan number recursively
    Catalan number are used in many combinatorial problems

    :param n:
    :return: nth catalan number
    """
    if n == 0:
        return 1
    return sum(catalan(i)*catalan(n-1-i) for i in range(n))


@cache_decorator
def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


if __name__ == '__main__':
    start_time = time.time()
    print(catalan(100))
    print(catalan(100))
    print("{} seconds".format(time.time()-start_time))
