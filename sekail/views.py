from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
)

from .serializers import (
    UserCreateSerializer,
    UserSerializer,
    UserUpdateSerializer,
   
)

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST


from .models import (
    User,
    Device,
    Store,
    Customer
    )


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer


class UserUpdateAPIView(RetrieveUpdateAPIView):
    
    def put(self, request, format=None):
        print(request.data)
        user= request.user
        serializer = UserUpdateSerializer(user , data= request.data, )
        if serializer.is_valid():
            serializer.save()
            return Response(UserSerializer(user,context={'request': request}).data, status=HTTP_200_OK)
        print(serializer.errors)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
