from omdb_wrapper import omdb_wrapper
from api_key import api_key
import pytest

test_wrapper = omdb_wrapper(api_key)


@pytest.fixture
def movie_title():
    movie_title: str = "toy story"
    return movie_title


@pytest.fixture
def movie_id():
    movie_id: str = "tt0114709"
    return movie_id


# Test search_movie_title method return
def test_search_movie_title(movie_title):
    assert test_wrapper.search_movie_title(movie_title) == "&t=toy%20story"


# Test search_movie_id method return
def test_search_movie_id(movie_id):
    assert test_wrapper.search_movie_id(movie_id) == "&i=tt0114709"


# Test build_dict_from_api building successful dictionary
def test_build_dict_from_api(movie_title):
    search_title_test = test_wrapper.search_movie_title(movie_title)
    test_wrapper.build_dict_from_api(search_title_test)
    assert len(test_wrapper.movie_dict) > 2
