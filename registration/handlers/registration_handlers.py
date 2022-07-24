from django.contrib.auth import get_user_model

from registration.entities.registration_entities import RegisterInputEntity
from rest_framework.exceptions import ValidationError

User = get_user_model()


class RegistrationHandler:

    def register(self, input_entity: RegisterInputEntity) -> User:
        user = User(username=input_entity.username)
        user.set_password(input_entity.password)
        user.save()
        return user
