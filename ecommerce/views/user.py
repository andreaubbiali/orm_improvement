from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from utils.user_utils import UserRegistrationSerializer
from rest_framework.permissions import AllowAny

@api_view(['POST'])
# @permission_classes([AllowAny])
def register_user(request):
    if request.method == 'POST':
        # serializer = UserRegistrationSerializer(data=request.data)

        return Response({"message": "Hello, world!"}, status=status.HTTP_201_CREATED)
        
        # if serializer.is_valid():
        #     serializer.save()  # Save the new user to the database
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)