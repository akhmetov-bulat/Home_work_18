from models import Movie, MovieSchema
from flask_restx import Resource, Namespace
from setup_db import db

movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

movie_ns = Namespace('movies')

@movie_ns.route('/')
class MovieView(Resource):
    def get(self):
        pass

    def post(self):
        pass

@movie_ns.route('/<int:mid>')
class MovieViewMid(Resource):
    def get(self,mid):
        pass

    def put(self,mid):
        pass

    def delete(self):
        pass



