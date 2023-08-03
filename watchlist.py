import requests
import dotenv
import os
import pandas as pd

dotenv.load_dotenv('.env')

def get_movie_id(api_key, movie_name):
    base_url = "https://api.themoviedb.org/3/search/movie"
    params = {"api_key": api_key, "query": movie_name}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if any results were found
        if data["total_results"] > 0:
            # Get the TMDB ID of the first result
            movie_id = data["results"][0]["id"]
            return movie_id
        else:
            # print(f"No results found for the movie '{movie_name}'")
            return None

    except requests.exceptions.RequestException as e:
        # print(f"Error while fetching movie details: {e}")
        return None

def get_watch_providers(api_key, movie_id, region):
    base_url = f"https://api.themoviedb.org/3/movie/{movie_id}/watch/providers"
    params = {"api_key": api_key}

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()

        # Check if watch providers information is available
        if "results" in data and region in data["results"]:
            region_data = data["results"][region]
            if "flatrate" in region_data:
                providers = [provider["provider_name"] for provider in region_data["flatrate"]]
                return providers
            else:
                # print(f"No streaming providers found for {region} (India) for this movie.")
                return None
        else:
            # print(f"Watch providers information not available for {region} (India) or this movie.")
            return None

    except requests.exceptions.RequestException as e:
        # print(f"Error while fetching watch providers information: {e}")
        return None


if __name__ == "__main__":
    api_key = os.getenv('TMDB_API')  # Replace this with your TMDB API key

    movieNames = pd.read_csv('watchlist.csv')['Name']
    region = 'US'

    for movieName in movieNames:
        movie_id = get_movie_id(api_key, movieName)
        if movie_id:
            streaming_providers = get_watch_providers(api_key, movie_id, region)
            if streaming_providers:
                with open('watchlistProviders.txt', 'a') as f:
                    f.write("{}: {}\n".format(movieName, streaming_providers))