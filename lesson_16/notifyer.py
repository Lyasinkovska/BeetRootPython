"""
Кода до 10ти строк. использование: notifier = notify(every=1000) создали нотификатор и внутри цикла дергаем его а
он каждые 1000 раз выводит "Итерация __ выполнена" (используется при генерации допустим большого файла чтоб видеть на
какой стадии процесс)
"""


def count_squares(stop):
    for j in range(stop):
        yield j ** 2


def write_to_file(number, filename='generator.txt'):
    with open(filename, 'a') as file:
        file.write(f'next_number: {number}\n')


def notify(every=1000):
    counter = 0
    const_every = every
    while True:
        yield every
        if counter % every == 0 and counter > 0:
            print('notify:', every)
            every += const_every
        counter += 1


if __name__ == '__main__':
    res = count_squares(100)
    n = notify(every=10)
    for i in res:
        next(n)
        print(i)

    notifier = notify()
    for numb in range(10000):
        write_to_file(numb)
        next(notifier)




