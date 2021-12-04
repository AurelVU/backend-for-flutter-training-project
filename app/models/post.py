from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from app.models.comment import Comment
from app.models.like import Like
from app.models.init_db import db


@db.Model.registry.mapped
@dataclass(init=False)
class Post:
    __table__ = db.Table(
        "post",
        db.Model.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
        db.Column("title", db.String(50)),
        db.Column("text", db.String(5000)),
        db.Column('time_created', db.DateTime(timezone=True), server_default=db.func.now()),
    )

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.title = kwargs.get('title')
        self.text = kwargs.get('text')
        self.time_created = kwargs.get('time_created', None)
        self.comments = kwargs.get('comments', [])
        self.likes = kwargs.get('likes', [])

    title: str
    text: str
    comments: List[Comment] = field(
        metadata=dict(
            dump_only=True
        )
    )
    likes: List[Like] = field(
        metadata=dict(
            dump_only=True
        )
    )
    id: Optional[int] = field(default=0, metadata=dict(dump_only=True, required=False))
    user_id: Optional[int] = field(default=0, metadata=dict(dump_only=True))
    time_created: Optional[datetime] = field(
        default=None,
        metadata=dict(
            dump_only=True
        )
    )

    __mapper_args__ = {  # type: ignore
        "properties": {
            "comments": db.relationship("Comment"),
            "likes": db.relationship("Like"),
        }
    }
