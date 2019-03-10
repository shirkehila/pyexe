from math import log10, pow


def check_id(id):
    """Checks if an id number is valid

    :param id: id number
    :return: True for valid id, otherwise false
    """
    # example 54370042-1
    check = id % 10  # 1
    id = int(id / 10)  # 54370042
    _sum = 0
    for i in range(8):
        next = (id%10) * (2 - i % 2)
        id=int(id/10)
        if next > 9:
            next = int(next / 10) + next % 10
        _sum += next
    sum_round_10 = pow(int(log10(_sum))+1, 10)
    return sum_round_10 == check


if __name__ == "__main__":
    id = input("Enter id to check")
    if check_id(int(id)):
        print("Valid")
    else:
        print("Invalid")
