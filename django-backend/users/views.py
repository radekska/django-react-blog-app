from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import RegisterUserSerializer


class CustomUserCreate(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        register_serializer = RegisterUserSerializer(data=request.data)
        if register_serializer.is_valid():
            new_user = register_serializer.save()
            if new_user:
                return Response(status=status.HTTP_201_CREATED)
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BlacklistTokenView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        try:
            refresh_token = request.data.get("refresh_token", None)
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(data="Token added to a blacklist.", status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)
