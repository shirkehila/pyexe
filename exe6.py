from pprint import pprint as pp


def times2(x): return x * 2


def mod2(x): return x % 2


def map_func(mapping, *args):
    l = args[0]
    mapped = [mapping(x) for x in l]
    return mapped


if __name__ == '__main__':
    pp(map_func(times2, [4, 7, 2, 9, 4]))
    pp(map_func(mod2, [4, 7, 2, 9, 4]))
