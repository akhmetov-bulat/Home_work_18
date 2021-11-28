from setup_db import db
from marshmallow import Schema, fields



class Movie(db.Model):
    __tablename__ = 'movies'
    id = db.Column(db.Integer, primaty_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(400))
    trailer = db.Column(db.String(100))
    year = db.Column(db.Integer(4))
    rating = db.Column(db.String(10))
    genre_id = db.Column(db.Integer, ForeignKey('genres.id'))
    director_id = db.Column(db.Integer, ForeignKey('directors.id'))


class MovieSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Str()
    genre_id = fields.Int()
    directori_id = fields.Int()

