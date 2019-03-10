lookup = {}


def catalan(n):
    """A function to calculate catalan number recursively
    Catalan number are used in many combinatorial problems

    :param n:
    :return:
    """
    # if we already computed this value
    if n in lookup:
        return lookup[n]
    # otherwise
    else:
        # compute the term
        if n == 0:
            value = 1
        else:
            value = sum(catalan(i)*catalan(n-1-i) for i in range(n))
        # store and return it
        lookup[n] = value
        return value


if __name__ == '__main__':
    print(catalan(100))
