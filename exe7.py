def catalan(n):
    """A function to calculate catalan number recursively
    Catalan number are used in many combinatorial problems

    :param n:
    :return:
    """
    if n == 0:
        return 1
    return sum(catalan(i)*catalan(n-1-i) for i in range(n))


if __name__ == '__main__':
    print(catalan(3))
