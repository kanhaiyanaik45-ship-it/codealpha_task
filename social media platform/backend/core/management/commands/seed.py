from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Profile, Post, Comment, Like


class Command(BaseCommand):
    help = 'Seed the database with sample data'

    def handle(self, *args, **options):
        if User.objects.filter(username='alice').exists():
            self.stdout.write('Seed data already exists')
            return

        alice = User.objects.create_user('alice', email='alice@example.com', password='password')
        bob = User.objects.create_user('bob', email='bob@example.com', password='password')
        # Profiles are auto created by signals
        Post.objects.create(author=alice.profile, content='Hello from Alice')
        p2 = Post.objects.create(author=bob.profile, content='Bob joins the platform')
        Comment.objects.create(post=p2, author=alice.profile, content='Welcome Bob!')
        Like.objects.create(post=p2, user=alice.profile)
        alice.profile.bio = 'Hi, I\'m Alice.'
        alice.profile.save()
        bob.profile.bio = 'Bob here.'
        bob.profile.save()
        self.stdout.write(self.style.SUCCESS('Seeded sample data'))