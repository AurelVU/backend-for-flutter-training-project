from dataclasses import dataclass, field

from app.models.init_db import db


@db.Model.registry.mapped
@dataclass
class URL:
    __table__ = db.Table(
        "url",
        db.Model.metadata,
        db.Column("id", db.Integer, primary_key=True),
        db.Column("post_id", db.Integer, db.ForeignKey("post.id")),
        db.Column("url", db.String(1000)),
    )
    url: str
    post_id: int = field(init=False)
    id: int = field(init=False)
