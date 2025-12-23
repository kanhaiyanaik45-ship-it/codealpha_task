from django.test import TestCase
from django.contrib.auth.models import User
from core.models import Profile, Post, Comment, Like


class CoreModelsTest(TestCase):
    def test_profile_created(self):
        u = User.objects.create_user('testuser', password='pass')
        self.assertTrue(hasattr(u, 'profile'))

    def test_create_post_and_comment_like(self):
        u = User.objects.create_user('u1', password='pass')
        p = Post.objects.create(author=u.profile, content='test')
        self.assertEqual(Post.objects.count(), 1)
        c = Comment.objects.create(post=p, author=u.profile, content='hi')
        self.assertEqual(Comment.objects.count(), 1)
        like = Like.objects.create(post=p, user=u.profile)
        self.assertEqual(Like.objects.count(), 1)
