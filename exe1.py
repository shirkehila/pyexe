from pprint import pprint as pp
nums_codes = {}  # a dictionary to hold card nums and codes


def load_codes():
    """Load number vs code dictionary from codes file
    """
    with open("nums_codes.txt") as nc:
        for record in nc:
            (num, code, balance) = record.split()
            nums_codes[num] = (code, int(balance))


def check_num_code(num, code):
    """Check if the code matches the card number

    :param num: card number
    :param code: card code
    :return: True if the code is correct, False otherwise
    """
    if nums_codes[num] == code:
        return True
    return False


if __name__ == '__main__':
    load_codes()
    pp(nums_codes)
