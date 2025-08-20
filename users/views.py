from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

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
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "avatar": user.avatar.url if user.avatar else None,
                "bio": user.bio,
                "is_host": user.is_host
            },
            "tokens": {
                "refresh": str(refresh),
                "access": str(access)
            }
        }, status=status.HTTP_201_CREATED)
