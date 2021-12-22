# IMDB Movies REST API

This project implements a REST API to obtain data from the top ranked movies in Internet Movie Database (IMDB).

The created database contains the following data: rank, IMDB id (it can be useful to search any other information required), title, IMDB rating, countries, directors, star actors, runtime, year, and genres. 
It has the records of the first 20 movies from the Top 250 IMDB Movies.

The information was obtained consuming the IMDB API (https://imdb-api.com/api). 

## Dependencies

The file named Pipfile contains all the dependencies needed. It can be loaded having the package "pipenv" installed.
The other option is to install through pip all the packages listed on requirements.txt.

* Python version: 3.8.10
* Packages:
  - requests: 2.26.0
  - flask: 2.0.2
  - flask-sqlalchemy: 2.5.1
  - flask-marshmallow: 0.14.0
  - marsmallow-sqlalchemy: 0.26.1

# Testing

The file __"routes.py"__ has the implemented endpoints with its methods. I performed the test requests using Postman, a free software that can be executed on a web browser.
To do that, you'll have to add a pair key-value in the headers ("Content-Type": application/json) and configure the body of the request as a raw json.

It's important to note that if you want to add some new movies to the database, there is a daily limit of 100 requests to the IMDB API for free users. To automate this process, you can use the script __"imdb.py"__ and change the _upper_limit_ and _lower_limit_ values (0 represents the movie ranked #1 and so on). 

## Methods

The following table indicates the methods implemented and its respective routes. 

| Method | Description | Route |
|--------|-------------|-------|
 GET (by rank)    | Given a rank, it returns the corresponding movie. |  _http:/localhost:port/movie/rank/\<rank>_
 GET (all) | It returns all the movies stored on the database | _http:/localhost:port/movie/_
 | GET (by country) | It returns a list of the movies filmed in the specified country | _http:/localhost:port/movie/countries/\<country>_
 | GET (by director) | It returns a list of movies directed by the specified director | _http:/localhost:port/movie/director/\<director>_
 | GET (by actor) | It returns a list of movies starred in by the given actor | _http:/localhost:port/movie/actor/\<actor>_
 GET (by genre) | Given a certain genre, it returns all the movies with that genre | _http:/localhost:port/movie/genre/\<genre>_
 | POST | It allows to add a new movie to the database | _http:/localhost:port/movie/_
 | PUT (by rank) | It modifies all the information from a movie with a given rank position | _http:/localhost:port/movie/rank/\<rank>_
 | DELETE (by rank) | It deletes the movie specified by rank from the database | _http:/localhost:port/movie/rank/\<rank>_