from django.urls import path,include
from rest_framework import routers
from .views import * 


router = routers.DefaultRouter()
router.register(r'perfumes', PerfumesView)

urlpatterns = [
    path('', include(router.urls)),
    path('perfumes/', views.PerfumeViewSet.as_view({'get': 'list'}), name='perfume-list'),
]
