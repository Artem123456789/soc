from rest_framework.exceptions import APIException

from comments.models import CommentUpvote, CommentDownvote
from comments.models import Comment
from django.contrib.auth import get_user_model

User = get_user_model()


class CommentsHandler:

    def upvote(self, comment: Comment, user: User):
        user_upvote = CommentUpvote.objects.filter(user=user, comment=comment)
        if len(user_upvote) > 0:
            raise APIException("User already is upvoted")

        user_downvote = CommentDownvote.objects.filter(user=user, comment=comment)
        if len(user_downvote) > 0:
            user_downvote.delete()

        new_upvote = CommentUpvote(user=user, comment=comment)
        new_upvote.save()

    def downvote(self, comment: Comment, user: User):
        user_downvote = CommentDownvote.objects.filter(user=user, comment=comment)
        if len(user_downvote) > 0:
            raise APIException("User already is downvoted")

        user_upvote = CommentUpvote.objects.filter(user=user, comment=comment)
        if len(user_upvote) > 0:
            user_upvote.delete()

        new_downvote = CommentDownvote(user=user, comment=comment)
        new_downvote.save()
