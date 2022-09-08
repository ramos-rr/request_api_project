import requests


class SwapiApiConsumer:

    @classmethod
    def get_starships(cls, page: int) -> any:
        params = {'page': page}
        response = requests.get('https://swapi.dev/api/starships/', params=params)

        return response.json()