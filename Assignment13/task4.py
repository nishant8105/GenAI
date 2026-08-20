# import library
import requests
import pandas as pd
from dotenv import load_dotenv
import os

# load env variable for API key
load_dotenv()

API_TOKEN = os.getenv("TMDBKEY")

if not API_TOKEN:
    raise ValueError("TMDBKEY not found in .env file")

headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}

# Fetch data of popular movies
popular_url = "https://api.themoviedb.org/3/movie/popular"

params = {
    "language": "en-US",
    "page": 1
}

response = requests.get(
    popular_url,
    headers=headers,
    params=params,
    timeout=30
)
# print status code of API
print("Popular Movies Status Code:", response.status_code)

response.raise_for_status()


# converting response from API to json
data = response.json()

# All popular movies
movie_data = []

for movie in data["results"]:
    movie_data.append({
        "Movie Title": movie.get("title"),
        "Release Date": movie.get("release_date"),
        "Rating": movie.get("vote_average"),
        "Popularity": movie.get("popularity"),
        "Vote Count": movie.get("vote_count")
    })

# fetching top rated movies form API
top_rated_url = "https://api.themoviedb.org/3/movie/top_rated"

response = requests.get(
    top_rated_url,
    headers=headers,
    params=params,
    timeout=30
)

print("Top Rated Movies Status Code:", response.status_code)

response.raise_for_status()

top_rated_data = response.json()

# Top-rated movies
top_rated_movies = []

for movie in top_rated_data["results"]:
    top_rated_movies.append({
        "Movie Title": movie.get("title"),
        "Release Date": movie.get("release_date"),
        "Rating": movie.get("vote_average"),
        "Popularity": movie.get("popularity"),
        "Vote Count": movie.get("vote_count")
    })


# print dataframe of Popular movise and top rated movies
df_movies = pd.DataFrame(movie_data)

df_top_rated = pd.DataFrame(top_rated_movies)



print("\nPopular Movies:")
print(df_movies)

print("\nTop Rated Movies:")
print(df_top_rated)

# saving popular movies and top rated movies to csv file
df_movies.to_csv("tmdb_movies.csv", index=False)

df_top_rated.to_csv("tmdb_top_rated_movies.csv", index=False)

print("\nCSV files successfully created!")