from django.urls import path
from .views import RequestListView, RequestCreateView

urlpatterns = [
    path('requests/', RequestListView.as_view(), name='request_list'),
    path('requests/create/', RequestCreateView.as_view(), name='request_create'),
]