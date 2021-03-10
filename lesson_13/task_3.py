"""
Write a function called `choose_func` which takes a list of nums and 2 callback functions. If all nums inside the list
are positive, execute the first function on that list and return the result of it. Otherwise, return the result of the
second one

# Assertions
assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]
assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]
"""


def is_all_positive(nums: list):
    return all(map(lambda elem: elem > 0, nums))


def choose_func(nums: list, func1, func2):
    funcs = {True: func1, False: func2}
    return funcs.get(is_all_positive(nums))(nums)


def square_nums(nums: list):
    return [num ** 2 for num in nums]


def remove_negatives(nums: list):
    return [num for num in nums if num > 0]


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [1, -2, 3, -4, 5]
    x = choose_func(nums1, square_nums, remove_negatives)
    print(x)
    y = choose_func(nums2, square_nums, remove_negatives)
    print(y)
    print(choose_func([], square_nums, remove_negatives))
