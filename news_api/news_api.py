# My own modules.
from .keys import Keys

# Other modules.
import requests


class NewsApi:
    """Collecting news."""
    # see https://newsapi.org
    parameters = {
        "country": "YOUR_COUNTRY",
        "apikey": "YOUR_API_KEY",
        "pageSize": 10
    }
    URL = "http://newsapi.org/v2/top-headlines"

    def __init__(self):
        response = NewsApi.get_response()
        json_data = response.json()
        self.articles = json_data[Keys.articles_key]

    @staticmethod
    def get_response():
        response = requests.get(
            NewsApi.URL,
            params=NewsApi.parameters,
        )
        response.raise_for_status()
        return response
