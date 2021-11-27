import marshmallow_dataclass

from app.models import User

UserSchema = marshmallow_dataclass.class_schema(User)
