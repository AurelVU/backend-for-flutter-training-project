import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.schema import PostSchema
from app.models import Post
from app.models.init_db import db

from .init_guard import guard

post_ns = Namespace('post', description='Операции для взаимодействия с постами')


@post_ns.route("/")
class PostsResource(Resource):
    @post_ns.doc('Get posts')
    @responds(schema=PostSchema, many=True, api=post_ns)
    def get(self):
        return db.session.query(Post).all()

    @flask_praetorian.auth_required
    @post_ns.doc('Get posts', security='Bearer')
    @accepts(schema=PostSchema, api=post_ns)
    def post(self):
        post = request.parsed_obj
        post.user_id = guard.extract_jwt_token(guard.read_token())['id']
        db.session.add(post)
        db.session.commit()
        return {'status': 'ok'}


@post_ns.route("/<int:post_id>")
class PostResource(Resource):
    @post_ns.doc('Get posts', params={'post_id': 'ID поста'})
    @responds(schema=PostSchema, api=post_ns)
    def get(self, post_id):
        return db.session.query(Post).get(post_id)
