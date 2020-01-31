import requests
import urllib.parse


class omdb_wrapper:
    # Init omdb_wrapper object with api_key from Omdb
    def __init__(self, api_key: str):
        self.movie_dict: dict = {}
        self.movie_list: list = []
        self.api_key: str = "?apikey=" + api_key
        self.target_url: str = "http://www.omdbapi.com/"
        self.input_error: str = "Please submit a valid input"
        self.movie_sort_types: dict = {
            "score": ["low_to_high", "high_to_low"],
            "title": ["a_to_z", "z_to_a"],
            "year": ["old_to_new", "new_to_old"],
        }
        self.movie_query_types: dict = {"id": "&i=", "title": "&t="}
        self.movie_search_types: list = [
            "actor",
            "director",
            "genre",
            "country",
            "language",
            "production studio",
        ]

    # Set new api_key for omdb_wrapper object
    def set_new_api_key(self, api_key: str):
        if type(api_key) == str and len(api_key) == 8:
            self.api_key: str = api_key
        else:
            return self.input_error

    # Create dict from API JSON response based off of input query
    def build_dict_from_api(self, url_query: str):
        if url_query == self.input_error:
            return self.input_error
        url: str = self.target_url + self.api_key + url_query
        api_response: requests.Response = requests.get(url)
        self.movie_dict: dict = api_response.json()

    # Find movie from title string (ex. 'Toy Story')
    def create_movie_search_url(self, type: str, movie_query: str) -> str:
        movie_query_converted: str = urllib.parse.quote(movie_query)
        if type in self.movie_query_types:
            url_query: str = self.movie_query_types[type] + movie_query_converted
            return url_query
        else:
            return self.input_error

    # Rank movies in direction based on type and return
    def sort_movies(self, type: str, direction: str) -> list:
        if type in self.movie_sort_types and direction in self.movie_sort_types[type]:
            self.movie_list.clear()
            # add correct typed movies to return list in order of direction
            return self.movie_list
        else:
            return [self.input_error]

    # Return list of movies with query
    def search_movies(self, type: str, query: str) -> list:
        if type in self.movie_search_types and type(query) == str:
            self.movie_list.clear()
            # add correct typed movies to return list if query matches
            return self.movie_list
        else:
            return [self.input_error]

    # TODO: Other API Features
