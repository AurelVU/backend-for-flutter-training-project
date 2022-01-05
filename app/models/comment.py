from .init_db import db


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"))
    text = db.Column(db.String(5000))
    time_created = db.Column('time_created', db.DateTime(timezone=True), server_default=db.func.now())

    author = db.relationship("User")
