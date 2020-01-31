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


# Test create_movie_search_url method return
def test_create_movie_search_url_from_title(movie_title):
    assert (
        test_wrapper.create_movie_search_url("title", movie_title) == "&t=toy%20story"
    )


# Test create_movie_search_url method return
def test_create_movie_search_url_from_id(movie_id):
    assert test_wrapper.create_movie_search_url("id", movie_id) == "&i=tt0114709"


# TODO Update Tests
