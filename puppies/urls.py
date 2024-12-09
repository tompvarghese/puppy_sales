from django.urls import path
from .views import PuppyListView, PuppyDetailView

urlpatterns = [
    path('puppies/', PuppyListView.as_view(), name='puppy-list'),
    path('puppies/<int:pk>/', PuppyDetailView.as_view(), name='puppy-detail'),
]
