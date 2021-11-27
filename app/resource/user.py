import flask_praetorian
from flask import request
from flask_accepts import responds, accepts
from flask_restx import Resource

from app import api
from app.models import User
from app.schema import UserSchema


@api.route("/restx/make_a_widget")
class UserResource(Resource):
    @flask_praetorian.auth_required
    @api.doc('Get all the conditions', security='Bearer')
    @accepts("Widget", dict(name="some_arg", type=str), schema=UserSchema, api=api)
    @responds(schema=UserSchema, api=api, status_code=201)
    def post(self):
        return request.parsed_obj
