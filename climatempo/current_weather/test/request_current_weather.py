from climatempo.city_id.test.request_city_id import mock_city_id


class CurrentWeatherRequestSpy:

    @staticmethod
    def get_weather():
        return {"id": 3877, "name": "Jundiaí", "state": "SP", "country": "BR", "data": {
                 "temperature": 18,
                 "wind_direction": "NE",
                 "wind_velocity": 9,
                 "humidity": 88,
                 "condition": "Trovoada e chuva",
                 "pressure": 1018,
                 "icon": "6",
                 "sensation": 18,
                 "date": "2022-09-13 10:41:00"}}
