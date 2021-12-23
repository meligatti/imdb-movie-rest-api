from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from myapp import app

import os


basedir = os.path.abspath(os.path.dirname(__name__))
# Configure database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'top_movies.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)
# Init Marshamallow model
ma = Marshmallow(app)

str_limits = {
    'title': 70,
    'imdb_id': 11,
    'countries': 60,
    'directors': 150,
    'genres': 90,
    'runtime_str': 8,
    'stars': 200
}

# Define the model of the database columns
class TopMovie(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rank = db.Column(db.Integer, unique = True, nullable = False)
    title = db.Column(db.String(str_limits['title']), unique = True, nullable = False)
    year = db.Column(db.Integer, nullable = False)
    imdb_rating = db.Column(db.Float(precision = 3))
    imdb_id = db.Column(db.String(str_limits['imdb_id']), unique = True)
    countries = db.Column(db.String(str_limits['countries']))
    directors = db.Column(db.String(str_limits['directors']))
    genres = db.Column(db.String(str_limits['genres']))
    runtime_str = db.Column(db.String(str_limits['runtime_str']))
    stars = db.Column(db.String(str_limits['stars']))

    def __init__(self, rank, title, year, 
                imdb_rating, imdb_id, countries,
                directors, genres,
                runtime_str, stars):
    
        self.rank = rank
        self.title = title
        self.year = year
        self.imdb_rating = imdb_rating
        self.imdb_id = imdb_id
        self.countries = countries
        self.directors = directors
        self.genres = genres
        self.runtime_str = runtime_str
        self.stars = stars

# Create the model to serialize data
class MovieSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'year', 
                  'countries', 'rank', 'runtime_str',
                  'imdb_rating', 'directors', 'stars',
                  'genres', 'imdb_id')

# This line has to be executed just for first time to create the database.
#db.create_all()

# Init Schema
movie_schema = MovieSchema()
movies_schema = MovieSchema(many = True)