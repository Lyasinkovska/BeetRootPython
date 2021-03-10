def read_file(file_name):
    with open(file_name) as file:
        print(file.read())


if __name__ == '__main__':
    read_file('my_file.txt')
