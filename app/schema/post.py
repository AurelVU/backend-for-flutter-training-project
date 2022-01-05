from marshmallow.fields import Nested
from marshmallow_sqlalchemy import auto_field

from app.schema.comment import CommentSchema
from app.schema.like import LikeSchema
from app.schema.url import URLSchema
from app.schema.short_user import ShortUserSchema
from app.schema.init_ma import ma
from app.models import Post


class PostSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Post
        load_instance = True
        include_fk = True
        include_relationships = True

    comments = Nested(CommentSchema, dump_only=True, many=True)
    author = Nested(ShortUserSchema, dump_only=True)
    likes = Nested(LikeSchema, dump_only=True, many=True)
    photos_url = Nested(URLSchema, many=True)

    id = auto_field(dump_only=True)
    user_id = auto_field(dump_only=True)
    time_created = auto_field(dump_only=True)
    title = auto_field()
    text = auto_field()
