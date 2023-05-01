from django.urls import include, path
from rest_framework.routers import SimpleRouter
from rest_framework_nested import routers

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
ads_router.register('ads', AdViewSet)
comments_router = routers.NestedSimpleRouter(ads_router, 'ads', lookup='ad')
comments_router.register('comments', CommentViewSet)

urlpatterns = [
	path("", include(ads_router.urls)),
	path("", include(comments_router.urls))]
