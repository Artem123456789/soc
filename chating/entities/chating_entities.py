from dataclasses import dataclass


@dataclass
class SendMessageInputEntity:
    text: str
    to_username: str


@dataclass
class GetChatInputEntity:
    chat_user_username: str


@dataclass
class SentMessageEntity:
    text: str
    sender_username: str
    receiver_username: str
