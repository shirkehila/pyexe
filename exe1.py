from pprint import pprint as pp
nums_codes = {}  # a dictionary to hold card nums and codes


def load_codes():
    """Load number vs code dictionary from codes file
    """
    with open("nums_codes.txt") as nc:
        for record in nc:
            (key, val) = record.split()
            nums_codes[key] = val


if __name__ == '__main__':
    load_codes()
    pp(nums_codes)
