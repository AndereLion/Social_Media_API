from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from rest_framework import generics, viewsets, status, mixins
from rest_framework.decorators import action, api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.renderers import JSONRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.settings import api_settings

from user.models import UserProfile
from user.serializers import UserSerializer, AuthTokenSerializer, UserProfileSerializer, UserProfileListSerializer


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
    serializer_class = AuthTokenSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self) -> Request:
        return self.request.user


class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer) -> None:
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == "list":
            return UserProfileListSerializer

        return self.serializer_class


@api_view(["GET"])
def toggle_following(request, pk):
    my_user = get_user_model().objects.get(id=request.user.id)
    gest_user = get_user_model().objects.get(id=pk)
    if my_user in gest_user.profile.followers.all():
        gest_user.profile.followers.remove(my_user.id)
    else:
        gest_user.profile.followers.add(my_user.id)
    return HttpResponse(status=status.HTTP_200_OK)


class UserFollowersViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        my_user = get_user_model().objects.get(id=self.request.user.id)
        return my_user.profile.followers.all()


class UserFollowingViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return self.queryset.filter(profile__followers=self.request.user.id)
