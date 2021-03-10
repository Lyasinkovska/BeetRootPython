def add_number(alist: list, adder: int = 1) -> list:
    ind = len(alist) - 1
    while ind >= 0:
        alist[ind] += adder
        adder = 0
        if alist[ind] > 9:
            adder = alist[ind] // 10
            alist[ind] = alist[ind] % 10
        ind -= 1
    if adder > 0:
        alist = [adder, *alist]
    return alist


if __name__ == '__main__':
    print(add_number([1, 2, 9], 1000))
    print(add_number([9, 9]))
