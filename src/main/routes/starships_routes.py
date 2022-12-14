"""
ROUTES: Is the main ROUTE that every request will pass by!
Indicate here all paths to API know how to behave
Indicate here all PAGES and addresses to the WEB APPLICATION
"""
from fastapi import APIRouter, Request as RequestFastApi
from fastapi.responses import JSONResponse, HTMLResponse
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.validators.get_starship_id_validator import get_starship_id_validator
from src.main.adapters.request_adapter import request_adapter
from src.main.composers.get_starship_in_pagination_composer import get_starships_in_pagination_composer
from src.main.composers.get_starship_information_composer import get_starship_information_composer
from src.presenters.errors.error_controller import handle_errors
from fastapi.templating import Jinja2Templates


starships_routes = APIRouter()
templates = Jinja2Templates(directory='src/main/templates')


@starships_routes.get('/', response_class=HTMLResponse)
async def home(request: RequestFastApi):
    """
    Homepage
    """
    return templates.TemplateResponse("home/home.html", {"request": request})


@starships_routes.get('/api/starships/list')
# async def means that some requests will have to wait the response, that it can't be so fast otherwise is going to fail
async def get_starships_in_pagination(request: RequestFastApi):
    """
    Get Starship paginator
    """
    # 1. INITIATE CONTROLER TO CALL EVERYONE
    controller = get_starships_in_pagination_composer()

    response = None
    try:
        # 2. VALIDATE PAMETERS WITH VALIDATOR:
        validator = get_pagination_validator(request)

        # 3. GET A BODY AND THE PAGE, AND FITS HTTP WITH ADAPTER. THEN CALL USING controller
        response = await request_adapter(request, controller.handle_page_parameter)

    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response["status_code"],
        content={"data": response["data"]}
    )


# Theis route is better with GET method, but we're going to use a POST method
@starships_routes.post("/api/starships/")
async def get_starship_information(request: RequestFastApi):
    """
    Get information from a specific starship through its ID
    """
    # COMPOSE EVERYTHING TOGETHER AND CONTROL
    controller = get_starship_information_composer()

    try:
        # VALIDATE PARAMS INPUT
        validator = await get_starship_id_validator(request)

        # TELL WHICH STARSHIP ID TO SEARCH USING ADAPTER THAT ALLOWS A PARAM AND A BODY TO BE BUILT
        response = await request_adapter(request=request, callback=controller.handle_starshp_info_parameter)

    except Exception as error:
        response = handle_errors(error)

    return JSONResponse(
        status_code=response["status_code"],
        content={"data": response["data"]}
    )
