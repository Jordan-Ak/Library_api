from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename = 'UserView',)
router.register('authors', views.AuthorViewSet, basename = 'AuthorView')