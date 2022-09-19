# Request Api Project

Based on tutorials from Programador Lhama in [YouTube](https://www.youtube.com/watch?v=MtyDUwJTkNE&list=PLAgbpJQADBGLG_ap3sbYefUp8HsiTt6Kf)
### New feature:<br>
- PyLint: need a `.pylint` file to work. Type `$pylint --generate-rcfile > .pylintrc` to generate it<br>
- Pre-commit: need a `.pre-commit.config.yaml`. Create it manually and copy YAML code;<br>
<br>
#### To avoid PYTEST from request on internet every commit, we need to MOCK!<br>

- Install [requests_mock](https://pypi.org/project/requests-mock/): Run `$ pipenv install requests-mock`
- Edit PYTEST FUNCTION you want to mock and add requests_mock as a parameter to activate it: `def test_get_starship(requests_mock)`
- First, implement simple test with requests only using GET method directly;<br>
- Then, use a more sophisticated method for GET, using `req_row = requests.Request(metohd='GET', url='url_desired', params='parameter_desided')`;<br>
- After that, use `prepare()` function to ajust format, like this: `req_prepared = req_row.prepare()`;<br>
- Finnaly, make a new function to get this prepared request and to ajust it in format HTTP to be sent online:<br>

```
from requests import Request
from typing import Type

def __send_http_requests(cls, req_prepared: Type[Request]) -> any:
    http_session = requests.Session()
    response = http_session.send(req_prepared)
    return response
```

<br>

- Now, it's time to protect your response to avoid it being altered by any override. Here,
we'll use [namedtuple()](https://docs.python.org/3/library/collections.html#collections.namedtuple):<br>

```
from collections import namedtuple

class SwapiApiConsumer:
    def __init__(self) -> None:
        self.get_starships_response = namedtuple('GET_Starships', 'status_code resquest response'
        
    
    def get_starships(self, page: int) -> None:
        # ...
        return self.get_starships_response(
                status_code = response.status_code,
                request = req_row,
                response = response.json()
        )
```

## CONFIG FASTAPI<br>
- Set up a route:<br>

```
<file: app.route.py>
from fastapi import APIRouter, Request as RequestFastApi

starships_routes = APIRouter()

@starships_routes.get('/')
def home(request: RequestFastApi):
    """
    Homepage
    """
    return {'message': 'Olá mundo'}
    
starships_routes.get('/api/starships/list')
def get_starships_in_paginator(request: RequestFastApi):
    """
    Get Starship paginator
    """
    print(request.query_params['page'])
    print(request.query_params['ola'])
    return {'Olá': 'Mundo'}
```
<br>
- Set up HTTP Config, pointing to the route:<br>

```
<file: app.http_serve_config.py>
from fastapi import FastAPI
from src.main.routes import starships_routes


app = FastAPI()

app.include_router(starships_routes)
```
<br>
- Run it with uvicorn to raise a server!<br>

```
<file: run.py>
import uvicorn

if __name__ == '__main__':
    uvicorn.run(
        "src.main.config.http_server_configs:app",
        host='127.0.0.1',
        port=8000,
        reload=True,
        debug=True,
        workers=3
    )
```
<br>

- <b>ADAPTER</b> DEFINING AN ADAPTOR IS DEFINING A BRIDGE BETWEEN FASTAPI AND A METHOD INSIDE OUR INTERNAL PROGRAM 
(USERCASE)<br>
-