import marshmallow_dataclass

from app.models import Comment

CommentSchema = marshmallow_dataclass.class_schema(Comment)
