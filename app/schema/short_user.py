from marshmallow_sqlalchemy import auto_field

from app.schema.init_ma import ma
from app.models import User


class ShortUserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

    id = auto_field(dump_only=True)
    hashed_password = auto_field(load_only=True)
