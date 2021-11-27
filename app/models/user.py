from dataclasses import dataclass
from typing import List, Optional

from app.models.init_db import db
from app.models.post import Post


@db.Model.registry.mapped
@dataclass
class User:
    __table__ = db.Table(
        "user",
        db.Model.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("name", db.String(50)),
        db.Column("hashed_password", db.String(255)),
        db.Column("website", db.String(255)),
        db.Column("firstname", db.String(50)),
        db.Column("lastname", db.String(50)),
        db.Column("nickname", db.String(12)),
    )
    id: int
    roles: str
    nickname: str
    firstname: str
    lastname: str
    hashed_password: str
    website: str
    posts: List[Post]

    __mapper_args__ = {  # type: ignore
        "properties": {
            "posts": db.relationship("Post")
        }
    }

    @property
    def identity(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has an ``identity`` instance
        attribute or property that provides the unique id of the user instance
        """
        return self.id

    @property
    def rolenames(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has a ``rolenames`` instance
        attribute or property that provides a list of strings that describe the roles
        attached to the user instance
        """
        try:
            return self.roles.split(",")
        except Exception:
            return []

    @property
    def password(self):
        """
        *Required Attribute or Property*
        flask-praetorian requires that the user class has a ``password`` instance
        attribute or property that provides the hashed password assigned to the user
        instance
        """
        return self.hashed_password

    @classmethod
    def lookup(cls, nickname):
        """
        *Required Method*
        flask-praetorian requires that the user class implements a ``lookup()``
        class method that takes a single ``username`` argument and returns a user
        instance if there is one that matches or ``None`` if there is not.
        """
        return cls.query.filter_by(nickname=nickname).one_or_none()

    @classmethod
    def identify(cls, user_id):
        """
        *Required Method*
        flask-praetorian requires that the user class implements an ``identify()``
        class method that takes a single ``id`` argument and returns user instance if
        there is one that matches or ``None`` if there is not.
        """
        return cls.query.get(user_id)
