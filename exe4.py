from itertools import groupby


def compress(str):
    """Compresses a string by letter,count,letter,count...

    :param str: a string to compress
    :return: compressed string
    """
    letters = list(str)
    compressed = ["{}{}".format(cnt, sum(1 for _ in group))
                  for cnt, group in groupby(letters)]
    return "".join(compressed)


if __name__ == "__main__":
    print(compress("aabbbbcdddeaaaaa"))
