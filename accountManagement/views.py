from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from accountManagement.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema

# Create your views here.


@swagger_auto_schema(
    method='get',
    responses={
        status.HTTP_200_OK: openapi.Response(
            'Response example (model):', UserSerializer),
    },
)
@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            'Response example (model):', UserSerializer)
    }
)
@api_view(['POST', 'GET'])
def signup(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = get_object_or_404(
                User, username=serializer.validated_data['username'])
            user.set_password(serializer.validated_data['password'])
            user.save()
            token = Token.objects.create(user=user)

            return Response({'user': serializer.data, 'token': token.key}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='get',
    responses={
        status.HTTP_200_OK: openapi.Response(
            'Response example (model):', UserSerializer),
    },
)
@swagger_auto_schema(
    method='post',
    request_body=UserSerializer,
    responses={
        status.HTTP_201_CREATED: openapi.Response(
            'Response example (model):', UserSerializer)
    }
)
@api_view(['GET', 'POST'])
def login(request):
    if request.method == 'POST':
        user = get_object_or_404(User, username=request.data['username'])
        if user.check_password(request.data['password']):
            serializer = UserSerializer(instance=user)
            token = get_object_or_404(Token, user=user)
            return Response({'user': serializer.data, 'token': token.key})
    return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)


@swagger_auto_schema(
    method='GET',
    responses={status.HTTP_200_OK: openapi.Response('Success')},
    manual_parameters=[
        openapi.Parameter(
            'Authorization', in_=openapi.IN_HEADER,
            type=openapi.TYPE_STRING,
            description='Token <your-token-value>',
            required=False,
        ),
    ],
)
@api_view(['GET'])
@authentication_classes([SessionAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def testToken(request):
    return Response({'detail': 'Success'})
