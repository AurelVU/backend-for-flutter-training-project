from marshmallow.fields import Nested
from marshmallow_sqlalchemy import auto_field

from app.models import Comment
from app.schema.init_ma import ma
from app.schema.short_user import ShortUserSchema


class CommentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Comment
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)
    author = Nested(ShortUserSchema, dump_only=True)
    user_id = auto_field(dump_only=True)
    post_id = auto_field(dump_only=True)
    time_created = auto_field(dump_only=True)
