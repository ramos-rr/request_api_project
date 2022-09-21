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


def mock_starship_info():
    """
     Mocked data for Starship Information dictionary
    :return Data from this starship
    """
    return {
        "name": fake.name(),
        "model": fake.name(),
        "max_atmosphering_speed": fake.random_int(),
        "hyperdrive_rating": fake.random_int(),
        "MGLT": fake.random_int(),
    }


class SwapiApiConsumerSpy:
    """
    Mock for SwapiApiCOnsumer
    """
    def __init__(self):
        self.get_starships_response = namedtuple(typename='GET_Starships', field_names='status_code, request, response')
        self.get_starship_info_response = namedtuple(typename='GET_Starship_Info',
                                                     field_names='status_code, request, response')
        self.get_starships_atributes = {}
        self.get_starship_info_atributes = {}

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

    def get_starship_information(self, starship_id: int) -> 'GET_Starship_Info':
        """
        Mock get_starship_information
        :param starship_id: Starship ID
        :return: A dictionary with starship information
        """
        self.get_starship_info_atributes["starship_id"] = starship_id
        return self.get_starship_info_response(
            status_code=200,
            request=None,
            response=mock_starship_info()
        )
