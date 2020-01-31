# Omdb.wrapper
[![Build status](https://travis-ci.org/sheikhisaac/Omdb.wrapper.svg?branch=master)](https://travis-ci.org/sheikhisaac)

Python wrapper class for Omdb movie database API

## Features
- Builds configured via Travis CI/CD

- Git hooks configured with Pre-Commit

- Streamlined API calls to organise data for Movie searches

- Batches Movie searches into search history

- Provides Movie search history sorted by Metacritic rating, alphabetically by title, or by year

- Provides Actor, Director, Genre, Country, Language, and Production Studio searches in search history

## Prerequisites

Ensure you are running Python 3.7.1

```zsh
$ python3 --version # returns 'Python 3.7.1'
```

Use pipenv to install all required pip3 packages from Pipfile and create virtual environment

```zsh
$ pipenv install
```

Use pipenv to access functions

```zsh
$ pipenv shell
```

Set up git hooks for pre-commit checks notated in .pre-commit-config.yaml

```zsh
$ pre-commit install
```

## Usage

Run the main functions

```python
from omdb_wrapper import omdb_wrapper

api_key = 'xxxxxxxx'
# instantialises jeopardy_parser object
test_wrapper = omdb_wrapper(api_key)

# creates dictionary of results from omdb api request from a movie title and appends to search history
test_wrapper.build_dict_from_api(test_wrapper.create_movie_search_url('title', 'Toy Story'))

# sort search history dictionary by year and return list
test_wrapper.sort_movies('year', 'new_to_old')

# return list of movie titles from search history dictionary with provided search type and query
test_wrapper.search_movies('actor', 'chris pratt')
```

Run the unit tests

```zsh
$ pytest -v
```

## Contact Info

```python
self.name = 'Isaac Sheikh'
self.email = 'sheikhisaac@gmail.com'
self.phone = '571-315-1881'
```

## Potential Next Steps

- Add additional tests to allow committing against pre-commit hooks if requirements change
- Update pre-commit yaml file to account for future improvements
