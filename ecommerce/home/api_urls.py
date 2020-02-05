from django.urls import path,include
from rest_framework import routers

from.views import UserViewSet,ItemViewSet,ItemFilterListView

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('item', ItemViewSet)

urlpatterns=[
    path('',include(router.urls)),
    path('items',ItemFilterListView.as_view(), name='items'),
]

