from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from instagram.models import Post
from instagram.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following = get_user_model().objects.filter(profile__followers=user.id)

        return Post.objects.filter(Q(author=user) | Q(author__in=following))

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def user_posts(self, request, *args, **kwargs):
    #     user = self.request.user
    #     posts = Post.objects.filter(author=user)
    #     serializer = PostSerializer(posts, many=True)
    #     return Response(serializer.data)
