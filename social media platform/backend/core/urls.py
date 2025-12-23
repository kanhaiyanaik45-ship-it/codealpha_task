from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from . import api_views

router = DefaultRouter()
router.register('posts', api_views.PostViewSet, basename='api-posts')
router.register('comments', api_views.CommentViewSet, basename='api-comments')
router.register('profiles', api_views.ProfileViewSet, basename='api-profiles')
router.register('likes', api_views.LikeViewSet, basename='api-likes')

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('follow/<str:username>/', views.follow_toggle, name='follow_toggle'),
    path('post/create/', views.create_post, name='create_post'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/like/', views.like_toggle, name='like_toggle'),
    path('api/', include(router.urls)),
]
