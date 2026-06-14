from django.urls import path
from .views import RequestListView

urlpatterns = [
    path('requests/', RequestListView.as_view(), name='request-list'),
]