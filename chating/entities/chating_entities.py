from dataclasses import dataclass


@dataclass
class SendMessageInputEntity:
    text: str
    to_username: str
