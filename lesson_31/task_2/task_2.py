"""
Load data
Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .
As a result, store all comments in chronological order in JSON and dump it to a file."""
import datetime
import json
from json.decoder import JSONDecodeError

import requests


def get_request_text(url: str, parameter: str) -> dict:
    resp = requests.get(url, {'subreddit': parameter})
    return resp.json()


def get_comments(request_text: dict) -> list:
    comments = []
    for res in request_text["data"]:
        time = datetime.datetime.fromtimestamp(res['created_utc']).strftime("%d %b %Y, %H:%M:%S")
        comments.insert(0, {time: res["body"]})
    return comments


def get_comments_from_reddit(url: str, param: str) -> list:
    return get_comments(get_request_text(url, param))


def upload_from_json(filename: str) -> list:
    if JSONDecodeError:
        return []
    else:
        with open(filename, 'r') as f:
            uploaded_file = json.load(f)
        return uploaded_file


def remove_duplicates(new_text: list, uploaded_text: list) -> list:
    for comment in new_text:
        if comment not in uploaded_text:
            uploaded_text.append(comment)
    return uploaded_text


def save_to_json_file(text: list, filename: str) -> None:
    uploaded = upload_from_json(filename)
    text = remove_duplicates(text, uploaded)
    with open(filename, 'w') as file:
        json.dump(text, indent=2, fp=file)


if __name__ == '__main__':
    URL = 'https://api.pushshift.io/reddit/comment/search/'
    subreddit = "socialskills"
    file_name = 'reddit_comments_socialskills.json'

    comms = get_comments_from_reddit(URL, param=subreddit)
    save_to_json_file(comms, file_name)
