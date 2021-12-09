"""User Model."""

from masoniteorm.models import Model


class User(Model):
    """User Model."""

    __fillable__ = ["username", "email", "password"]

    __auth__ = "username"
