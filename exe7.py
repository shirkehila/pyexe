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
    """A function to calculate fibonacci number recursively

    :param n:
    :return: nth fibonacci number
    """
    if n == 0 or n == 1:
        return 1
    return fib(n-1)+fib(n-2)


@cache_decorator
def padovan(n):
    """A function to calculate padovan numbers
    as n grown padovan(n)/padovan(n-1) approaches the plastic number

    :param n:
    :return: nth padovan number
    """
    if n == 0 or n == 1 or n == 2:
        return 1
    return padovan(n-2)+padovan(n-3)


if __name__ == '__main__':
    start_time = time.time()
    print(padovan(100))
    print("{} seconds".format(time.time()-start_time))
