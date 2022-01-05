from app.models.init_db import db


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    title = db.Column(db.String(50))
    text = db.Column(db.String(5000))
    time_created = db.Column(db.DateTime(timezone=True), server_default=db.func.now())

    comments = db.relationship("Comment", uselist=True)
    author = db.relationship("User")
    likes = db.relationship("Like", uselist=True)
    photos_url = db.relationship("URL", uselist=True)
