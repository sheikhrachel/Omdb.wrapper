import requests
import urllib.parse


class omdb_wrapper:
    # Init omdb_wrapper object with api_key from Omdb
    def __init__(self, api_key: str):
        self.movie_dict: dict = {}
        self.target_url: str = "http://www.omdbapi.com/"
        self.api_key: str = "?apikey=" + api_key

    # Set new api_key for omdb_wrapper object
    def set_new_api_key(self, api_key: str):
        self.api_key: str = api_key

    # Find movie from title string (ex. 'Toy Story')
    def search_movie_title(self, movie_title: str):
        movie_title_converted: str = urllib.parse.quote(movie_title)
        url_title_query: str = "&t=" + movie_title_converted
        return url_title_query

    # Find movie from IMDB ID (ex. tt0114709)
    def search_movie_id(self, movie_id: str):
        movie_id_converted: str = urllib.parse.quote(movie_id)
        url_id_query: str = "&i=" + movie_id_converted
        return url_id_query

    # Create dict from API JSON response based off of input queries
    def build_dict_from_api(self, url_query: str):
        url: str = self.target_url + self.api_key + url_query
        api_response: requests.Response = requests.get(url)
        self.movie_dict: dict = api_response.json()

    # Print movie(s) from movie_dict
    def print_movie_list(self):
        if len(self.movie_dict) < 3:
            print("No valid list of movies yet!")
        else:
            for field in self.movie_dict:
                print(field, self.movie_dict[field])

    # TODO: Other API Features
