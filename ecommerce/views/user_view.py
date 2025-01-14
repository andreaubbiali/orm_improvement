from rest_framework.response import Response
# from rest_framework import status
from rest_framework.decorators import api_view
from ecommerce.utils.user_util import UserRegistrationSerializer
# from rest_framework.permissions import AllowAny
from ecommerce.models import User

@api_view(['POST'])
# @permission_classes([AllowAny])
def register_user(request):
    
    # todo catch unique contraint violation

        serializer = UserRegistrationSerializer(data=request.data)

        if serializer.is_valid():
            
            user = User(
                username=serializer.validated_data['username'],
                email=serializer.validated_data['email'],
                password=serializer.validated_data['password'],
                phone=serializer.validated_data['phone'],
                address=serializer.validated_data['address'],
            )

            print(user)

            user.save()

            user_data = UserRegistrationSerializer(user).data

            return Response({
                'status': 'success',
                'message': 'User registered successfully.',
                'user': user_data
            }, status=201)
        
        else:

            return Response({
                'status': 'error',
                'message': 'Validation failed.',
                'errors': serializer.errors
            }, status=400)
