"""
Implement binary search using recursion.
"""


def binary_search(item, sorted_collection):
    if len(sorted_collection) == 0:
        return False
    else:
        middle = len(sorted_collection) // 2
    if item == sorted_collection[middle]:
        return True
    else:
        if item < sorted_collection[middle]:
            return binary_search(item, sorted_collection[:middle])
        else:
            return binary_search(item, sorted_collection[middle + 1:])


if __name__ == '__main__':
    collection = [i for i in range(100)]
    print(binary_search(99, collection))
    print(binary_search(120, collection))


