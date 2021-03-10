def file_read(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line


def stihi(*args):
    all_lines = []
    for arg in args:
        all_lines.append(file_read(arg))

    ok = True
    while ok:
        ok = False
        for one in all_lines:

            try:
                ret = next(one)
                yield ret
                ok = True
            except Exception:
                pass


if __name__ == '__main__':
    f = stihi('one.txt', 'two.txt', 'three.txt')
    for n in f:
        print(n)
