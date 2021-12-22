from __main__ import app

from models import TopMovie, movie_schema, movies_schema, db
from flask import request, jsonify

import pprint

# Get a single movie by rank
@app.route('/movie/rank/<int:rank>', methods = ['GET'])
def get_by_rank(rank):
    # The get method uses the primary key, so it's not suitable for this
    # kind of search.
    #movie = TopMovie.query.get(rank)
    #return movie_schema.jsonify(movie)
    movie = TopMovie.query.filter(TopMovie.rank == rank)
    result = movies_schema.dump(movie)
    return jsonify(result)

    
# Get all movies
@app.route('/movie', methods = ['GET'])
def get_all_movies():
    all_movies = TopMovie.query.order_by(TopMovie.rank).all()
    result = movies_schema.dump(all_movies)
    return jsonify(result)

# Get all movies by country
@app.route('/movie/countries/<string:country>', methods = ['GET'])
def get_all_movies_by_country(country):
    sel_country_movies = TopMovie.query.filter(TopMovie.countries.like('%' + country + '%'))
    result = movies_schema.dump(sel_country_movies)
    return jsonify(result)

# Get all movies by director
@app.route('/movie/director/<string:director>', methods = ['GET'])
def get_all_movies_by_director(director):
    sel_director_movies = TopMovie.query.filter(TopMovie.directors.like('%' + director + '%'))
    result = movies_schema.dump(sel_director_movies)
    return jsonify(result)

# Get all movies by actor
@app.route('/movie/actor/<string:actor>', methods = ['GET'])
def get_all_movies_by_actor(actor):
    sel_actor_movies = TopMovie.query.filter(TopMovie.stars.like('%' + actor +'%'))
    result = movies_schema.dump(sel_actor_movies)
    return jsonify(result)

# Get all movies by genre
@app.route('/movie/genres/<string:genre>', methods = ['GET'])
def get_all_movies_by_genre(genre):
    sel_genre_movies = TopMovie.query.filter(TopMovie.genres.like('%' + genre + '%'))
    result = movies_schema.dump(sel_genre_movies)
    return jsonify(result)

# Create a new movie in database
@app.route('/movie', methods = ['POST'])
def add_movie():
    rank = request.json['rank']
    title = request.json['title']
    year = request.json['year']
    imdb_rating = request.json['imDbRating']
    imdb_id = request.json['id']
    countries = request.json['countries']
    directors = request.json['directors']
    genres = request.json['genres']
    runtime_str = request.json['runtimeStr']
    stars = request.json['stars']

    new_movie = TopMovie(rank, title, year, imdb_rating,
                imdb_id, countries, directors,
                genres, runtime_str, stars)

    db.session.add(new_movie)
    db.session.commit()

    return movie_schema.jsonify(new_movie)

# Modify entire object
@app.route('/movie/rank/<int:rank>', methods = ['PUT'])
def modify_movie(rank):
    orig_movie_list = TopMovie.query.filter(TopMovie.rank == rank).all()
    orig_movie = orig_movie_list[0]

    new_rank = request.json['rank']
    title = request.json['title']
    year = request.json['year']
    imdb_rating = request.json['imDbRating']
    imdb_id = request.json['id']
    countries = request.json['countries']
    directors = request.json['directors']
    genres = request.json['genres']
    runtime_str = request.json['runtimeStr']
    stars = request.json['stars']

    orig_movie.rank = new_rank
    orig_movie.title = title
    orig_movie.year = year
    orig_movie.imdb_rating = imdb_rating
    orig_movie.imdb_id = imdb_id
    orig_movie.countries = countries
    orig_movie.directors = directors
    orig_movie.genres = genres
    orig_movie.runtime_str = runtime_str
    orig_movie.stars = stars

    db.session.commit()

    return movie_schema.jsonify(orig_movie)


# Modify the rank and the rating of a movie
@app.route('/movie/rank/<int:rank>', methods = ['PATCH'])
def modify_rank(rank):
    movie = TopMovie.query.filter(TopMovie.rank == rank).all()
    movie = movie[0]

    new_rank = request.json['rank']
    new_rating = request.json['imDbRating']
    movie.rank = new_rank
    movie.imdb_rating = new_rating

    db.session.commit() 

    return movie_schema.jsonify(movie)



# Delete a movie in database
@app.route('/movie/rank/<int:rank>', methods = ['DELETE'])
def delete_movie(rank):
    orig_movie_list = TopMovie.query.filter(TopMovie.rank == rank).all()
    movie = orig_movie_list[0]

    db.session.delete(movie)
    db.session.commit()

    return movie_schema.jsonify(movie)





