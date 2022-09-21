from cerberus import Validator
from src.errors import HttpUnprocessableEntityError


async def get_starship_id_validator(request: any):
    """ Validator for correct Starship params """

    try:
        body = await request.json()
    except:
        body = None

    # CREATING A VALIDATION SCHEMA:
    body_starship_id = Validator({
        "starship_id": {"type": "integer", "required": False}
    })

    # RESPONSE is going to be Boolean (True or False)
    response = body_starship_id.validate(body)
    if not response:
        print(f'Validation == {response}')
        print(f'body got == {body}')
        print(body_starship_id.errors)
        raise HttpUnprocessableEntityError(message=body_starship_id.errors)
    else:
        print(f'Validation == {response}')
