from rest_framework.response import Response
from rest_framework import status

def custom_response(data=None, code=None, message=None, status_code=status.HTTP_200_OK):
    if code is None:
        code = 200
    if message is None:
        message = "success"
    
    response_structure = {
        "code": code,
        "message": message,
        "data": data if data is not None else {}
    }
    return Response(response_structure, status=status_code)
    