"""
View functions of the app.
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpRequest
from rest.json_response import JSONResponseBuilder


@api_view(["GET", "POST"])
def query_result(request: HttpRequest, format: str=None) -> Response:
    """
    View function to show query result.
    """
    json_response = JSONResponseBuilder().build(request)
    return Response(json_response)
