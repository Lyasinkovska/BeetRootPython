"""Custom exception
Create your custom exception named `CustomException`, you can inherit from base Exception class, but extend its
functionality to log every error message to a file named `logs.txt`. Tips: Use __init__ method to extend
functionality for saving messages to file
```
class CustomException(Exception):
def __init__(self, msg):
...
"""
from datetime import datetime


class CustomException(Exception):
    def __init__(self, msg):
        self.add_log_msg(msg)

    def add_log_msg(self, msg):
        with open('logs.txt', 'a') as logs:
            logs.write(f'{datetime.today()}: {msg} \n')
        print(f'The log message "{msg}" was added.')


if __name__ == '__main__':
    first_exception = CustomException('First Error')
    second = CustomException('Second error')
    CustomException.add_log_msg(first_exception, "Custom")
