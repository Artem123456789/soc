from dataclasses import dataclass


@dataclass
class VotePostInputEntity:
    post_id: int


@dataclass
class CommentInputEntity:
    text: str
    user_id: int
    post_id: int
