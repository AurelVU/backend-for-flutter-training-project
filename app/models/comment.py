from dataclasses import dataclass, field
from datetime import datetime

from .init_db import db


@db.Model.registry.mapped
@dataclass
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
    id: int = field(init=False)
    user_id: int = field(init=False)
    post_id: int = field(init=False)
    text: str
    time_created: datetime = field(
        init=False,
        metadata=dict(
            dump_only=True
        )
    )
