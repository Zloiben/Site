from django import template
from django.contrib.auth.models import AnonymousUser
from django.core.handlers.wsgi import WSGIRequest
from django.utils.functional import SimpleLazyObject
from django.utils.safestring import mark_safe

from ..models import *

register = template.Library()


@register.simple_tag(name="get_like_image")
def get_like_image(request: WSGIRequest, post: Post):
    btn_login_like = mark_safe('''
    <button id="btn-icon-login" class="no-like" type="button" data-bs-toggle="modal" data-bs-target="#loginModal">
    </button>
    ''')

    if request.user.is_anonymous or not request.user.is_authenticated:
        return btn_login_like

    like = mark_safe('<button id="btn-icon" class="like" type="submit"></button>')
    no_like = mark_safe('<button id="btn-icon" class="no-like" type="submit"></button>')

    like_info = Like.objects.filter(post=post, author=request.user)
    if like_info:
        return like
    return no_like


@register.simple_tag(name="get_profile_image_or_btn_login")
def get_profile_image_or_btn_login(request: WSGIRequest):
    btn_login = mark_safe('''
    <button class="btn btn-outline-primary" type="button" data-bs-toggle="modal" data-bs-target="#loginModal">
                Login
    </button>''')

    if request.user.is_anonymous or not request.user.is_authenticated:
        return btn_login

    profile_modal = UserProfile.objects.get(user=request.user)
    profile_image = mark_safe(f'''
    <div class="mini-profile">
        <img class="mini-profile__image" src="{profile_modal.image.url}" alt="Изображение"
        aria-label="Image" title="Image"> 
        <p class="mini-profile__name">{profile_modal.user.username}</p>
    </div>
    ''')
    return profile_image

