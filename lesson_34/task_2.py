"""
Requests using concurrent and multiprocessing libraries

Download all comments from a subreddit of your choice using URL: https://api.pushshift.io/reddit/comment/search/ .

As a result, store all comments in chronological order in JSON and dump it to a file. For this task use concurrent and
multiprocessing libraries for making requests to Reddit API.
"""
import datetime
import json
import multiprocessing
from functools import partial

import requests

from lesson_34.task_1 import time_execution


def get_request_text(url: str, parameter: str) -> dict:
    resp = requests.get(url, {'subreddit': parameter})
    return resp.json()


def get_comments(request_text: dict) -> list:
    comments = []
    for res in request_text["data"]:
        time = datetime.datetime.fromtimestamp(res['created_utc']).strftime("%d %b %Y, %H:%M:%S")
        comments.insert(0, {time: res["body"]})
    return comments


@time_execution
def get_comments_from_reddit(url: str, params) -> list:
    pool = multiprocessing.Pool(processes=4)
    return pool.map(partial(get_request_text, url), params)


def save_to_json_file(text: list, filename: str) -> None:
    with open(filename, 'w') as file:
        json.dump(text, indent=2, fp=file)


if __name__ == '__main__':
    URL = 'https://api.pushshift.io/reddit/comment/search/'
    subreddits = ("socialskills", "CasualIreland", "RoastMe")
    file_name = 'reddit_comments_socialskills.json'

    comments = get_comments_from_reddit(URL, params=subreddits)
    save_to_json_file(comments, file_name)
