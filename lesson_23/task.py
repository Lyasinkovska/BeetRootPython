import json


def extract_coordinates(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        file = json.load(f)
    return file['features'][0]['geometry']['coordinates']


def reverse_coordinates(coordinates):
    for elem in coordinates:
        if type(elem[0]) == list:
            reverse_coordinates(elem)
        else:
            elem[0], elem[1] = elem[1], elem[0]
    return coordinates


def write_to_file(filename, new_coordinates):
    with open(filename, 'r', encoding='utf-8') as f:
        file = json.load(f)
    file['features'][0]['geometry']['coordinates'] = new_coordinates

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(file, f)


def write_reversed_coords(filename):
    new_file_content = reverse_coordinates(extract_coordinates(filename))
    write_to_file(filename, new_file_content)


if __name__ == '__main__':
    write_reversed_coords('ato.json')
