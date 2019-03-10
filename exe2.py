def sum1():
    """Sum a list of numbers input 1 by 1

    :return: the sum
    """
    _sum = 0
    num = input("Enter next number, to finish enter 'stop'")
    try:
        while num != "stop":
            _sum += int(num)
            num = input("Enter next number, to finish enter 'stop'")
    except ValueError:
        print("You entered something different than a number")
    return _sum


def sum2():
    """Sum a list of numbers in one input

    :return: the sum
    """
    nums = input("Enter a sequence of numbers separated by commas:")
    # remove whitespaces
    nums = "".join(nums.split(" "))
    nums = nums.split(",")
    if all(x.isdigit() for x in nums):
        nums = [int(num) for num in nums]
        return sum(nums)
    print("You entered something different than a number or wrong separator")
    return 0


if __name__ == "__main__":
    print("first sum is: {}".format(sum1()))
    print("second sum is: {}".format(sum2()))
