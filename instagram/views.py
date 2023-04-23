from django.contrib.auth import get_user_model
from django.db.models import Q, QuerySet
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from instagram.models import Post
from instagram.serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    @staticmethod
    def _params_to_ints(qs: str) -> list:
        """Converts a list of string IDs to a list of integers"""
        return [int(str_id) for str_id in qs.split(",")]

    def get_queryset(self) -> QuerySet:
        queryset = self.queryset
        hashtags = self.request.query_params.get("hashtags", None)
        if hashtags:
            hashtags_ids = self._params_to_ints(hashtags)
            queryset = queryset.filter(hashtags__id__in=hashtags_ids)

        user = self.request.user
        following = get_user_model().objects.filter(profile__followers=user.id)
        return queryset.filter(Q(author=user) | Q(author__in=following))

    def perform_create(self, serializer) -> None:
        serializer.save(author=self.request.user)
