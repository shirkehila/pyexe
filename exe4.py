from itertools import groupby


def compress(str):
    letters = list(str)
    compressed = ["{}{}".format(cnt, sum(1 for _ in group))
                  for cnt, group in groupby(letters)]
    return "".join(compressed)


if __name__ == "__main__":
    print(compress("aabbbbcdddeaaaaa"))
