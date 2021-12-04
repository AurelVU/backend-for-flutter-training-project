import flask_praetorian
from flask import request
from flask_accepts import responds, accepts
from flask_restx import Namespace, Resource

from app.schema import CommentSchema
from app.models import Comment
from app.models.init_db import db
from .init_guard import guard

comment_ns = Namespace('comment', description='Операции для взаимодействия с комментариями')


@comment_ns.route("/<int:post_id>")
class CommentResource(Resource):
    @comment_ns.doc('Get posts', params={'post_id': 'ID поста'})
    @responds(schema=CommentSchema, many=True, api=comment_ns)
    def get(self, post_id):
        return db.session.query(Comment).filter_by(post_id=post_id).all()

    @flask_praetorian.auth_required
    @comment_ns.doc('Get posts', params={'post_id': 'ID поста'}, security='Bearer')
    @accepts(schema=CommentSchema, api=comment_ns)
    def post(self, post_id):
        comment = request.parsed_obj
        comment.post_id = post_id
        comment.user_id = guard.extract_jwt_token(guard.read_token())['id']
        db.session.add(comment)
        db.session.commit()
        return {'status': 'ok'}


@comment_ns.route("/<int:post_id>/<int:comment_id>")
class PostResource(Resource):
    @comment_ns.doc('Get posts', params={'post_id': 'ID поста', 'comment_id': 'ID комментария'})
    @responds(schema=CommentSchema, api=comment_ns)
    def get(self, post_id, comment_id):
        return db.session.query(Comment).filter_by(post_id=post_id).filter_by(id=comment_id).first()
