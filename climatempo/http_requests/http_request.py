import requests


class HttpRequests:

    @classmethod
    def send_http_request(cls, request_prepared):
        http_session = requests.Session()
        response = http_session.send(request_prepared)
        return response
