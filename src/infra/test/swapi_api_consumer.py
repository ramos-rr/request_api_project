from faker import Faker
from collections import namedtuple

fake = Faker()


def mock_starships():
    """
     Mocked data for Starships
    :return Data from this starship
    """
    return {
        "name": fake.name(),
        "model": fake.name(),
        "manufacturer": fake.name(),
        "cost_in_credits": fake.random_int(),
        "length": fake.random_int(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
        "url": f"https://swapi.dev/api/starships/{fake.random_int()}/"
    }


class SwapiApiConsumerSpy:
    """
    Mock for SwapiApiCOnsumer
    """
    def __init__(self):
        self.get_starships_response = namedtuple(typename='GET_Starships', field_names='status_code, request, response')
        self.get_starships_atributes = {}

    def get_starships(self, page: int) -> any:
        """
        Mock to get starships
        :param page: Page desired
        :return: A dictionary with ship details
        """
        self.get_starships_atributes["page"] = page
        return self.get_starships_response(
            status_code=200,
            request=None,
            response={"results": [mock_starships()]}
        )

