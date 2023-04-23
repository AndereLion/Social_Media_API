from django.urls import path, include
from rest_framework import routers
from .views import (
    PostViewSet,

)

app_name = "instagram"
router = routers.SimpleRouter()
router.register("post", PostViewSet)
urlpatterns = [
    path("", include(router.urls)),

    # path("feed/", PostListView.as_view(), name="post-feed"),
    # path(
    #     "my-posts/",
    #     PostViewSet.as_view({"get": "user_posts"}),
    #     name="my_posts"
    # ),

    # path("<int:pk>/like/", like_post, name="like-post"),
    # path("liked/", LikedPostList.as_view(), name="liked-post-list"),
]
