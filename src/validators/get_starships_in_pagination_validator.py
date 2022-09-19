from cerberus import Validator


def get_pagination_validator(request: any):
    """Pagination validator"""

    # CREATING A VALIDATION SCHEMA:
    querry_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1', '2', '3', '4'], 'required': True},
    })

    # .validade() is a buit in function inside CERBERUS that returns TRUE if all conditions match with the request
    response = querry_param_validator.validate(request.query_params)
    if not response:
        raise Exception(querry_param_validator.errors)

    print(response)
