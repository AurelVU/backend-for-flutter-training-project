from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_praetorian import Praetorian
from flask_restx import Api

from app.config import BaseConfig
from app.schema import UserSchema
from .models.init_db import db

guard = Praetorian()
cors = CORS()
migrate = Migrate()
api = Api(authorizations={
    'Bearer': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization',
        'description': "Type in the *'Value'* input box below: **'Bearer &lt;JWT&gt;'**, where JWT is the token"
    },
})

from .resource import *
from .models import *


def create_app(config):
    config = BaseConfig  # Todo: fixme!!!

    app = Flask(__name__)
    app.config.from_object(config)
    app.debug = True
    from app.models import User
    with app.app_context():
        guard.init_app(app, User)

    db.init_app(app)
    migrate.init_app(app, db)
    api.init_app(app)

    cors.init_app(app)

    return app
