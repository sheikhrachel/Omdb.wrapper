# Omdb.wrapper
[![Build status](https://travis-ci.org/sheikhisaac/Omdb.wrapper.svg?branch=master)](https://travis-ci.org/sheikhisaac)

Python wrapper class for Omdb movie database API

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

## Usage

Run the main functions

```python
from omdb_wrapper import omdb_wrapper

api_key = 'xxxxxxxx'
# instantialises jeopardy_parser object
test_wrapper = omdb_wrapper(api_key)

# creates dict of results from omdb api request
test_wrapper.build_dict_from_api(test_wrapper.search_movie_title('Toy Story'))
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
