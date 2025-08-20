from rest_framework import viewsets, generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from .models import User
from .serializers import UserSerializer, RegisterSerializer

# CRUD для пользователей (только авторизованные)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

# Регистрация
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        refresh = RefreshToken.for_user(user)
        access = refresh.access_token

        return Response({
            "user": UserSerializer(user).data,
            "tokens": {
                "refresh": str(refresh),
                "access": str(access)
            }
        }, status=status.HTTP_201_CREATED)


class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            access = refresh.access_token
            return Response({
                "user": UserSerializer(user).data,
                "tokens": {
                    "refresh": str(refresh),
                    "access": str(access)
                }
            })
        return Response({"detail": "Неверные данные для входа"}, status=status.HTTP_401_UNAUTHORIZED)

class RefreshView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({"detail": "Нет токена для обновления"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access = refresh.access_token
            return Response({"access": str(access)})
        except Exception:
            return Response({"detail": "Неверный токен"}, status=status.HTTP_400_BAD_REQUEST)

