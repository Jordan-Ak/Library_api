from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register('users', views.UserViewSet, basename = 'UserView',)
router.register('authors', views.AuthorViewSet, basename = 'AuthorView')
router.register('publishers', views.PublisherViewSet, basename = 'PublisherView',)
router.register('genres', views.GenreViewSet, basename = 'GenreView')
router.register('books', views.BookViewSet, basename = 'BookView')
router.register('borrowed', views.BorrowedViewSet, basename = 'BorrowedView')
router.register('quantity', views.QuantityBookViewSet, basename = 'QuantityView')
router.register('rating', views.RatingViewSet, basename = 'RatingView')
router.register('time-borrowed', views.QuantityTimeViewSet, basename = 'TimeBorrowedView')