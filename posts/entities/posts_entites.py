from dataclasses import dataclass


@dataclass
class VotePostInputEntity:
    post_id: int


@dataclass
class CommentInputEntity:
    text: str
    post_id: int
