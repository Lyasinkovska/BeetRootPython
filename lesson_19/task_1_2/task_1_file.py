"""
File Context Manager class
Create your own class, which can behave like a built-in function `open`. Also, you need to extend its functionality
with counter and logging. Pay special attention to the implementation of `__exit__` method, which has to cover all
the requirements to context managers mentioned here:
"""
import logging


class File:
    counter = 0

    def __init__(self, filename, mode):
        self.__allowed_modes = ('r', 'r+', 'rb', 'w', 'w+', 'wb', 'wb+', 'a', 'a+', 'ab', 'ab+')
        self.mode = mode if mode in self.__allowed_modes else 'r'
        self.filename = filename
        self.closed = False

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        logging.basicConfig(filename='files/files_opened.log', level=logging.INFO, filemode='a',
                            format=f'%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        File.counter += 1
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f'file {File.counter}: {self.filename}, raised exception:({exc_type.__name__})')
        self.file.close()
        self.closed = True


if __name__ == '__main__':

    with File('files/new_file.txt', 'l') as f:
        print(f.read())

    with File('files/next_file.txt', 'w') as h:
        for i in range(5):
            h.write(f'Hello {i}\n')
    print(h.closed)
