from dataclasses import dataclass, field
from datetime import datetime

from .init_db import db


@db.Model.registry.mapped
@dataclass(init=False)
class Comment:
    __table__ = db.Table(
        "comment",
        db.Model.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
        db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
        db.Column("text", db.String(5000)),
        db.Column('time_created', db.DateTime(timezone=True), server_default=db.func.now()),
    )

    def __init__(self, **kwargs):
        self.id = kwargs.get('id', None)
        self.user_id = kwargs.get('user_id', None)
        self.post_id = kwargs.get('post_id', None)
        self.text = kwargs.get('text')
        self.time_created = kwargs.get('time_created', None)

    id: int = field(metadata=dict(dump_only=True))
    user_id: int = field(metadata=dict(dump_only=True))
    post_id: int = field(metadata=dict(dump_only=True))
    text: str
    time_created: datetime = field(
        metadata=dict(
            dump_only=True
        )
    )
