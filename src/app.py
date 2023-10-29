import argparse
from os import getenv

import requests

from config import SERVER, TOKEN, TOPIC


class Ntfy:
    def __init__(self, server: str, topic: str, token: str):
        self.server = server
        self.topic = topic
        self.token = token

    def send(
        self,
        message: str = "",
        title: str = "",
        priority: str = "high",
    ):
        message = message or getenv("MESSAGE", "")
        title = title or getenv("TITLE", "")
        response = requests.post(
            url=f"{self.server}/{self.topic}",
            data=message,
            headers={
                "Authorization": f"Bearer {self.token}",
                "t": title or message,
                "Priority": priority,
                "ta": "warning",
            },
        )
        print(response.status_code)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("ntfyc")
    parser.add_argument("message", help="Message", type=str)
    parser.add_argument("title", nargs="?", help="Title", type=str, default="")
    args = parser.parse_args()
    app = Ntfy(SERVER, TOPIC, TOKEN)
    app.send(args.message, args.title)
