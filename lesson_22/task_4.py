"""
Function returns reversed input string
reverse("hello") == "olleh"
    True
reverse("o") == "o"
    True
"""


def reverse(input_str: str) -> str:
    if len(input_str) < 2:
        return input_str
    return input_str[-1] + reverse(input_str[:-1])


if __name__ == '__main__':

    print(reverse("hello"))
    print(reverse('o'))
    print(reverse(''))
    print(reverse('0123456789'))