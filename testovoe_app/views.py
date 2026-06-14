from django.views.generic import ListView
from .models import Request

class RequestListView(ListView):
    model = Request
    context_object_name = 'requests'
    template_name = 'orders/request_list.html'
