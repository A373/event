from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import CustomUser, EventName


# Create your views here.
@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    email = request.POST.get('email', None)
    if email is None:
        content = {
            'message': 'email is mandatory'
        }
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        try:
            user = CustomUser.objects.get(email=email)
            content = {
                'user_id': user.id,
                'username': user.username,
                'phone': user.phone,
                'created': user.created,
            }
            return Response(content, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            context = {
                'message': 'enter valid email'
            }
            return Response(context, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@authentication_classes([JWTTokenUserAuthentication])
@permission_classes([IsAuthenticated])
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        if name is None:
            content = {
                'message': 'name is missing'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        if name.isalpha() is not True:
            content = {
                'message': 'name must be a string'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        try:
            new_event = EventName.objects.create(
                name=name,
            )
            new_event.save()
            content = {
                'data': {
                    'message': 'event has been created',
                    'name': new_event.name,
                }
            }
            return Response(content, status=status.HTTP_200_OK)
        except ValueError:
            content = {
                'message': 'name has to be string'
            }
            return Response(content, status=status.HTTP_400_BAD_REQUEST)
        # except IntegrityError:
        # content = {
        #    'message': 'invalid event_id'
        # }
        # return Response(content, status=status.HTTP_400_BAD_REQUEST)
