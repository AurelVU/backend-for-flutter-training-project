from marshmallow_sqlalchemy import auto_field

from app.schema.init_ma import ma
from app.models import URL


class URLSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = URL
        load_instance = True
        include_fk = True
        include_relationships = True

    id = auto_field(dump_only=True)
    post_id = auto_field(dump_only=True)
