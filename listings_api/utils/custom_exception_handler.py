from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from rest_framework.response import Response


class ServiceUnavailable(APIException):
    status_code = 503
    default_detail = 'Service temporarily unavailable, try again later. See Retry-After instructions.'
    default_code = 'service_unavailable'


def custom_exception_handler(exc, context=None):
    response = exception_handler(exc, context)
    if isinstance(exc, ServiceUnavailable):
        headers = {}
        headers['Retry-After'] = '%d' % 120
        return Response(response.data, status=exc.status_code, headers=headers)

    return response