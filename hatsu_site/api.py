from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from .serializer import *
from .models import *


class PostViewSet(ModelViewSet):
    lookup_field = 'slug'
    serializer_class = PostSerializer

    def get_queryset(self) -> list:
        slug = self.kwargs.get("slug")
        if not slug:
            return Post.objects.all()
        return Post.objects.filter(slug=slug)


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer

    def get_queryset(self) -> list:
        pk = self.kwargs.get("pk")
        if not pk:
            return Like.objects.all()
        return Like.objects.filter(pk=pk)

    @action(methods=['get'], detail=False, permission_classes=[],
            url_path='all-user/(?P<post>[^/.]+)', url_name='all_user', serializer_class=PostLikeSerializer)
    def get_post_likes(self, request: Request, post: int):
        """
        Всех кто поставил лайк на этот пост
        """
        return Response([
            {'pk': i.pk, 'post_id': i.post_id, 'user_id': i.author_id}
            for i in Like.objects.filter(post=post)])

    @action(methods=['delete'], detail=False, permission_classes=[],
            url_path='delete/(?P<post>[^/.]+)', url_name='all_user', serializer_class=PostLikeSerializer)
    def delete_like_post(self, request: Request, post: int):

        like_post = Like.objects.filter(post_id=post, author_id=1)
        if like_post:
            like_post.delete()
            return Response({'code': 'success delete'})
        return Response({'code': 'not found'})
