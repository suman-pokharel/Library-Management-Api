from argparse import Namespace
from .api_views import *
from django.urls import path, include
from rest_framework import routers


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'librarians', LibrarianViewSet)
router.register(r'books', BookViewSet)
router.register(r'borrow', BorrowViewSet)
router.register(r'category', CategoryViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api_auth/',include('rest_framework.urls',namespace='rest_framework'))
    
]