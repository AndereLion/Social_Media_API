from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from user.views import (
    UserProfileViewSet,
    toggle_following,
    UserFollowersViewSet,
    UserFollowingViewSet,
    CreateUserView,
    ManageUserView,
)

app_name = "user"
router = routers.SimpleRouter()
router.register("profile", UserProfileViewSet)
router.register("my_following", UserFollowingViewSet)
router.register("my_followers", UserFollowersViewSet)

urlpatterns = [
    path("", include(router.urls)),

    path("follow/<int:pk>/", toggle_following, name="toggle_following"),
    path("register/", CreateUserView.as_view(), name="create"),
    path("me/", ManageUserView.as_view(), name="manage"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
