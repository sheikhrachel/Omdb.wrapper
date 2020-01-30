from omdb_wrapper import omdb_wrapper
import pytest

api_key = "fake_key"
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
