from dataclasses import dataclass


@dataclass
class SendMessageInputEntity:
    text: str
    to_username: str


@dataclass
class GetChatInputEntity:
    sender_username: str
    receiver_username: str

