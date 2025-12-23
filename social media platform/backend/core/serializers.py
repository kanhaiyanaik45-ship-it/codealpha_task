from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Like


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    followers_count = serializers.IntegerField(source='followers.count', read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'avatar', 'followers_count')


class CommentSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'created_at')


class PostSerializer(serializers.ModelSerializer):
    author = ProfileSerializer(read_only=True)
    comments = CommentSerializer(source='comment_set', many=True, read_only=True)
    likes_count = serializers.IntegerField(source='like_set.count', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'author', 'content', 'created_at', 'comments', 'likes_count')


class LikeSerializer(serializers.ModelSerializer):
    user = ProfileSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'post', 'user', 'created_at')
