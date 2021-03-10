""" task 4
получаем в цикле 
число
действие
второе число
пишем промежутчный результат
запрашиваем действие 
и снова число
действие...
если вместо числа или действия введено Q выходим"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def get_number():
    while True:
        user_input = input("Enter number: ")
        if user_input.isnumeric():
            return int(user_input)
        elif user_input == "Q":
            return None
        else:
            print("Wrong number format.")
            continue


def get_action(action):
    actions = {"+": add, "-": subtract, "*": multiply}
    while True:
        action = input("Enter action: ")
        if action in actions.keys():
            return actions[action]
        elif action == "Q":
            return None
        elif action not in actions.keys():
            print("Wrong action.")
            continue


if __name__ == '__main__':

    total = get_number()
    while True:
        if total is None:
            break
        action = get_action()
        if action is None:
            break
        number = get_number()
        if number is None:
            break
        total = action(total, number)
        print(f"The result is: {total}. If you want to quit enter Q.")
