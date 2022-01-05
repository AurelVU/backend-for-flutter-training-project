import flask_praetorian

from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.schema import PostSchema
from app.models import Post, Like
from app.models.init_db import db

from .init_guard import guard

post_ns = Namespace('post', description='Операции для взаимодействия с постами')


@post_ns.route("/")
class PostsResource(Resource):
    @post_ns.doc('Get posts', params={'page': 'Номер страницы'})
    @responds(schema=PostSchema, many=True, api=post_ns)
    def get(self):
        query = db.session.query(Post).order_by(Post.time_created.desc())
        page = request.args.get('page')
        if page:
            query = query.limit(7).offset(int(page) * 7)
        return query.all()

    @flask_praetorian.auth_required
    @post_ns.doc('Get posts', security='Bearer')
    @accepts(schema=PostSchema, api=post_ns)
    def post(self):
        post = request.parsed_obj
        post.user_id = guard.extract_jwt_token(guard.read_token())['id']
        post.comments = []
        post.likes = []
        db.session.add(post)
        db.session.commit()
        return {'status': 'ok'}


@post_ns.route("/<int:post_id>")
class PostResource(Resource):
    @post_ns.doc('Get posts', params={'post_id': 'ID поста'})
    @responds(schema=PostSchema, api=post_ns)
    def get(self, post_id):
        return db.session.query(Post).get(post_id)


@post_ns.route("/<int:post_id>/like")
class LikePostResource(Resource):
    @flask_praetorian.auth_required
    @post_ns.doc('Like post', params={'post_id': 'ID поста'}, security='Bearer')
    def post(self, post_id):
        user_id = guard.extract_jwt_token(guard.read_token())['id']
        like = db.session.query(Like).filter(Like.post_id == post_id).filter(Like.user_id == user_id).first()
        if like:
            db.session.delete(like)
        else:
            db.session.add(Like(user_id=user_id, post_id=post_id))
        db.session.commit()
        return {'status': 'ok'}
