from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional, List

from app.models.comment import Comment
from app.models.like import Like
from app.models.init_db import db


@db.Model.registry.mapped
@dataclass
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
    id: int = field(init=False)
    user_id: int = field(init=False)
    title: str
    text: str
    time_created: datetime
    comments: List[Comment]
    likes: List[Like]

    __mapper_args__ = {  # type: ignore
        "properties": {
            "comments": db.relationship("Comment"),
            "likes": db.relationship("Like"),
        }
    }
