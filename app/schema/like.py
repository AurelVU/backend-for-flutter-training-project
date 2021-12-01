import marshmallow_dataclass

from app.models import Like

LikeSchema = marshmallow_dataclass.class_schema(Like)
