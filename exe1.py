from pprint import pprint as pp
nums_codes = {}  # a dictionary to hold card nums and codes
ops = ['a', 'b', 'c', 'd']
cur_num = ''


def load_codes():
    """Load number vs code dictionary from codes file
    """
    with open("nums_codes.txt") as nc:
        for record in nc:
            (num, code, balance) = record.split()
            nums_codes[num] = (code, int(balance))


def check_num_code():
    """Ask user for card number and code until he enters a correct pair or quits

    :param
    :param
    :return: True if the code is correct, False if quited
    """
    num = input("Enter card number:")  # card number
    code = input("Enter code:")  # card code
    global cur_num
    global nums_codes
    while nums_codes[num][0] != code:
        print("Wrong number, please try again:")
        num = input("Enter card number: (press q to quit)")
        if num == "q":
            return False
        code = input("Enter code: (press q to quit)")
        if code == "q":
            return False
    cur_num = num
    return True


def withdrawal():
    """Asks user how much money to withdrawal and withdrawals it

    :return:
    """
    global cur_num
    choice = input("How much money to withdrawal?\na - 20\nb - 50\nc - another")
    if choice == 'a':
        money = 20
    elif choice == 'b':
        money = 50
    else:
        money = int(input("Enter amount of money"))
    if money > nums_codes[cur_num][1]:
        print("Not enough money!")
    else:
        nums_codes[cur_num][1] -= money


if __name__ == '__main__':
    load_codes()
    exit_bank = 0  # 0 until the user wants to exit
    result = check_num_code()
    if result:
        while True:
            op = input("Choose operation:\na - print balance\nb - withdrawal\nc - change code\nd - quit")
            while op not in ops:
                print("Wrong operation, try again:")
                op = input("a - print balance\nb - withdrawal\nc - change code\nd - quit")
            if op == 'a':
                print("Your balance is {} dollars".format(nums_codes[cur_num][1]))
            elif op == 'b':
                withdrawal()
            else:
                break  # chose d



