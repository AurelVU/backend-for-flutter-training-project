import marshmallow_dataclass

from app.models import Post

AddressSchema = marshmallow_dataclass.class_schema(Post)
