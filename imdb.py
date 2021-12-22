#from typing_extensions import runtime
import requests
import pprint
import models
import json

# First, I want to get all the movies from the Top 250 IMDB Movies
# (Mainly to know their id's)

# As I could get the json file containing all the top movies, I prefered to get the information from there.
# However, you can find a block commented code to use the json response from the IMDB API.
f = open('top_movies.json')
movies_list = json.load(f)
movies_list = movies_list['items']

# Original code to consume Best Movies API
headers = {
    'Accepts': 'application/json'
} 

params = {
    'apiKey': 'k_e63z1cmm'
}

""" url_250_movies = 'https://imdb-api.com/en/API/Top250Movies/'

all_movies_response = requests.get(url = url_250_movies, params = params, headers = headers)
#pprint.pprint(all_movies_response.json())

movies_list = all_movies_response.json().get('items')
print(len(movies_list)) """

# Limit the amount of API calls (free users have 100 calls a day)
lower_limit = 20
upper_limit = 21

for i in range(lower_limit, upper_limit):
    current_movie = movies_list[i]
    rank = current_movie['rank']
    title = current_movie['title']
    year = current_movie['year']
    imdb_id = current_movie['id']
    rating = current_movie['imDbRating']

    # Now, use the previous id to use the other endpoint and fill the other information.
    single_movie_url = 'https://imdb-api.com/en/API/Title/'
    params['id'] = imdb_id

    single_response = requests.get(single_movie_url, headers = headers, params = params)

    # Add the additional information 
    countries = single_response.json().get('countries')
    directors = single_response.json().get('directors')
    genres = single_response.json().get('genres')
    runtime_str = single_response.json().get('runtimeStr')
    stars = single_response.json().get('stars')

    # Create the data dictionary to send json posts to the database
    movie_dict = {
        'rank': int(rank),
        'title': title,
        'year': int(year),
        'id': imdb_id,
        'imDbRating': float(rating),
        'countries': countries,
        'directors': directors,
        'genres': genres,
        'runtimeStr': runtime_str,
        'stars': stars
    }

    # Store the data into the database 
    test_headers = {'content-type': 'application/json'}
    local_url = 'http://127.0.0.1:5000/movie'
    local_server_response = requests.post(local_url, data = json.dumps(movie_dict), headers = test_headers) 
    print(local_server_response.status_code) 


