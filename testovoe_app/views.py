from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from .models import Request
from .forms import  RequestCreateForm

class RequestListView(ListView):
    model = Request
    context_object_name = 'requests'
    template_name = 'orders/request_list.html'

class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Request
    form_class = RequestCreateForm
    template_name = 'orders/request_form.html'
    success_url = reverse_lazy('request_list')
    success_message = "Заявка успешно создана!"
