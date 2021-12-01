import marshmallow_dataclass

from app.models import Post

PostSchema = marshmallow_dataclass.class_schema(Post)
