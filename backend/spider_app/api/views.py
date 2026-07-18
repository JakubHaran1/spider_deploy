from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated
from spider_app.models import User, Tag, Spider, Spider_img
from .serializers import UserSerializer, TagSerializer, SpiderSerializer, SpiderImgSerializer
from .permission import isAuthor
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(methods=["post"], detail=False)
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(request, username=username, password=password)
        if user is None:
            raise AuthenticationFailed("Credential's are not correct")

        token = RefreshToken.for_user(user)
        user_data = UserSerializer(user).data
        print(user_data)
        return Response({
            "access": str(token.access_token),
            "refresh": str(token),
            "user": user_data,
        })

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def me(self, request, pk=None):
        if request.user is None:
            return AuthenticationFailed("No user")
        return Response(UserSerializer(request.user, many=False).data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class SpiderImgViewSet(viewsets.ModelViewSet):
    queryset = Spider_img.objects.all()
    serializer_class = SpiderImgSerializer


class SpiderViewSet(viewsets.ModelViewSet):
    queryset = Spider.objects.all()
    serializer_class = SpiderSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering_fields = ['date_created', 'name', 'type']
    search_fields = ['name', 'author__username', 'type', 'tags__tag']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def get_permissions(self):
        if self.action == "update" or self.action == "partial_update" or self.action == "destroy":
            self.permission_classes = [isAuthor]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()
