import marshmallow_dataclass

from app.models import URL

URLSchema = marshmallow_dataclass.class_schema(URL)
