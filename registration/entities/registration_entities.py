from dataclasses import dataclass


@dataclass
class RegisterInputEntity:
    username: str
    password: str
    password_repeat: str


@dataclass
class RegisterResponseEntity:
    user_id: int
