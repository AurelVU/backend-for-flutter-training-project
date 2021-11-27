from dataclasses import dataclass
from .init_db import db


@db.Model.registry.mapped
@dataclass
class Like:
    __table__ = db.Table(
        "like",
        db.Model.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("user_id", db.Integer, db.ForeignKey("user.id")),
        db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
    )
    id: int
    user_id: int
    post_id: int
