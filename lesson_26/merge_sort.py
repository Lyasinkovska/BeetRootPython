"""
Implement the mergeSort function without using the slice operator.
"""


def merge_sort(array, left_index=0, right_index=None):
    right_index = right_index or len(array)

    if right_index - left_index > 1:

        middle = (left_index + right_index) // 2
        merge_sort(array, left_index, middle)
        merge_sort(array, middle, right_index)

        merged = []
        i = left_index
        j = middle
        while i < middle and j < right_index:
            if array[i] <= array[j]:
                merged.append(array[i])
                i = i + 1
            else:
                merged.append(array[j])
                j = j + 1

        merged.extend(array[i:middle])
        array[left_index:left_index + len(merged)] = merged
    return array


if __name__ == '__main__':
    array = [5, 1, 9, 3, 0]  # [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(merge_sort(array))
