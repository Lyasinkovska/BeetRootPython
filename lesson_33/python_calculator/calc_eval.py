from collections import deque

from lesson_24.stack import Stack

ERROR_MSG = 'ERROR'


class InfixToPostfix:

    def __init__(self, expression):
        self.expression = expression
        self.__operators = Stack()
        self.__output = []
        self.__precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, ')': 0, '(': 0}
        if self.__check_brackets():
            self.__convert()

    @property
    def result(self):
        return self.__output

    def __check_brackets(self):
        brackets = deque()
        for element in self.expression:
            if "(" in element:
                brackets.appendleft("(")
            elif ")" in element:
                if len(brackets) > 0:
                    brackets.pop()
                else:
                    return False

        if len(brackets) == 0:
            return True
        else:
            return False

    def __convert(self):
        for ind, char in enumerate(self.expression):
            if char.isdigit():
                if len(self.__output) and self.expression[ind-1].isdigit():
                    number = self.__output.pop() + char
                    self.__output.append(number)
                else:
                    self.__output.append(char)
            else:
                if self.__operators.is_empty:
                    self.__operators.push(char)
                else:
                    if char == '(' or self.__precedence[char] > self.__precedence[self.__operators.peek()]:
                        self.__operators.push(char)
                    else:
                        if char == ')':
                            while self.__operators.peek() != '(':
                                self.__output.append(self.__operators.pop())
                            self.__operators.pop()
                        else:
                            while len(self.__operators) and self.__precedence[char] <= self.__precedence[self.__operators.peek()]:
                                self.__output.append(self.__operators.pop())
                            self.__operators.push(char)

        while len(self.__operators) > 0:
            self.__output.append(self.__operators.pop())

        return self.__output


class EvaluatePostfix:

    def __init__(self, expression):
        self.expression = expression
        self.__operands = []
        self.__operations = {'+': lambda a, b: a + b,
                             '-': lambda a, b: b - a,
                             '/': lambda a, b: b / a,
                             '*': lambda a, b: a * b,
                             '^': lambda a, b: b ** a,
                             }
        self.__evaluate()

    @property
    def result(self):
        return self.__operands[0]

    def __evaluate(self):
        for char in self.expression:
            if char.isdigit():
                self.__operands.append(int(char))
            else:
                new_char = self.__operations[char](self.__operands.pop(), self.__operands.pop())
                self.__operands.append(new_char)


def evaluate(expression):
    postfix_exp = InfixToPostfix(expression).result
    try:
        return str(EvaluatePostfix(postfix_exp).result)
    except:
        return 'ERROR'


if __name__ == '__main__':
    exp = "10+5*6"
    print(InfixToPostfix(exp).result)
    print(evaluate(exp))
