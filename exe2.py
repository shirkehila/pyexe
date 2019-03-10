def sum1():
    """Sum a list of numbers input 1 by 1

    :return:
    """
    _sum = 0
    num = input("Enter next number, to finish enter 'stop'")
    while num != "stop":
        _sum += int(num)
        num = input("Enter next number, to finish enter 'stop'")
    return _sum


def sum2():
    """Sum a list of numbers in one input

    :return:
    """
    nums = input("Enter a sequence of numbers separated by commas:")
    # remove whitespaces
    nums = "".join(nums.split(" "))
    nums = nums.split(",")
    nums = [int(num) for num in nums]
    return sum(nums)


if __name__ == "__main__":
    print("first sum is: {}".format(sum1()))
    print("second sum is: {}".format(sum2()))
