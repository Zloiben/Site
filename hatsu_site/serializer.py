from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class PostLikeSerializer(serializers.Serializer):
    pk = serializers.IntegerField()
    post_id = serializers.IntegerField()
    user_id = serializers.IntegerField()
