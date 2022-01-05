from app.models import Like
from app.schema.init_ma import ma


class LikeSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Like
        load_instance = True
        include_fk = True
