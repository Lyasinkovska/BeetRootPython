import json
import os

import requests

filename = 'task_kmr/docs.json'


def create_file_path(document: dict) -> str:
    f_name = f"{document['name'].replace(' ', '_')}.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    dest_dir = os.path.join(script_dir, 'kmr_documents')

    try:
        os.makedirs(dest_dir)
    except OSError:
        pass
    path = os.path.join(dest_dir, f_name)
    return path


def download_documents(file_name: str = filename) -> None:
    with open(file_name) as f:
        file = json.load(f)

    for document in file:
        try:
            response = requests.get(document['link'])
        except:
            raise Exception('Wrong link')

        content = response.content
        path = create_file_path(document)

        with open(path, 'wb') as file:
            file.write(content)


if __name__ == '__main__':
    download_documents()
