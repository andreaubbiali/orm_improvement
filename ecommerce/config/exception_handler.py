from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from django.http import Http404
from django.core.exceptions import PermissionDenied
from rest_framework.exceptions import ValidationError

def custom_exception_handler(exc, context):
    """
    Custom exception handler for Django REST Framework.
    """
    # Let DRF's default exception handler process the exception first
    response = exception_handler(exc, context)

    print(exc)

    if response is None:
        # Handle exceptions not handled by DRF's default handler
        if isinstance(exc, Http404):
            return Response({'error': 'Resource not found'}, status=404)
        elif isinstance(exc, PermissionDenied):
            return Response({'error': 'Permission denied'}, status=403)
        elif isinstance(exc, APIException):
            return Response({'error': str(exc)}, status=exc.status_code)
        elif isinstance(exc, ValidationError):
            return Response({'error': 'Validation failed', 'details': str(exc)}, status=400)
        else:
            # For all other unhandled exceptions
            return Response({'error': 'An unexpected error occurred', 'details': str(exc)}, status=500)

    # Optionally, modify the default DRF response
    custom_data = {
        'status': 'error',
        'message': response.data.get('detail', 'An error occurred'),
        'errors': response.data
    }
    response.data = custom_data

    return response

# def handle_exception(self, exc):
#     # Custom handling of exceptions in the view.
