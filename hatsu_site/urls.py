from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page
from rest_framework import routers

from .api import *
from .views import *

router = routers.SimpleRouter()
router.register(r'post', PostViewSet, basename="post")
router.register(r'like', LikeViewSet, basename="like")
router.register(r'user', UserViewSet, basename='user')
router.register(r'category', CategoryViewSet, basename='category')


urlpatterns = [
    path('', Blog.as_view(), name='home'),
    path('post/<slug:post_slug>/', Post.as_view(), name='post'),
    path('api/v1/', include(router.urls))
]
