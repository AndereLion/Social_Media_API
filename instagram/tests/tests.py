from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth import get_user_model
from instagram.models import Post, Hashtag, Comment
from instagram.serializers import PostSerializer


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PostTests(APITestCase):
    def setUp(self):
        self.user = create_user(
            email="test@test.com",
            password="testpass",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_post(self):
        data = {"caption": "test post"}
        response = self.client.post(reverse("instagram:post-list"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get(reverse("instagram:post-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_retrieve_post(self):
        post = Post.objects.create(author=self.user, caption="test post")
        response = self.client.get(reverse("instagram:post-detail", args=[post.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        post = Post.objects.create(author=self.user, caption="test post")
        data = {"caption": "updated caption"}
        response = self.client.patch(reverse("instagram:post-detail", args=[post.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        post = Post.objects.create(author=self.user, caption="test post")
        response = self.client.delete(reverse("instagram:post-detail", args=[post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_hashtag_model(self):
        hashtag = Hashtag.objects.create(name="test")
        self.assertEqual(str(hashtag), hashtag.name)

    def test_comment_model(self):
        post = Post.objects.create(author=self.user, caption="test post")
        comment = Comment.objects.create(post=post, author=self.user, text="test comment")
        self.assertEqual(str(comment), comment.text)

    def test_post_serializer(self):
        post = Post.objects.create(author=self.user, caption="test post")
        serializer = PostSerializer(post)
        expected_fields = ["id", "author", "hashtags", "image", "caption", "created_at", "updated_at"]
        self.assertEqual(set(serializer.data.keys()), set(expected_fields))
