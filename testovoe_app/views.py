from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from .models import Request
from .forms import  RequestCreateForm

class RequestListView(ListView):
    model = Request
    context_object_name = 'requests'
    template_name = 'orders/request_list.html'
    paginate_by = 10

class RequestDetailsView(DetailView):
    model = Request
    template_name = 'orders/request_detail.html'
    context_object_name = 'req'

    def post(self, request, *args, **kwargs):
        req = self.get_object()
        new_status = request.POST.get('status')
        if new_status in dict(Request.STATUS_CHOICES):
            req.status = new_status
            req.save()
            messages.success(request, f"Статус заявки №{req.id} успешно изменен!")
        return redirect('request-detail', pk=req.id)

class RequestCreateView(SuccessMessageMixin, CreateView):
    model = Request
    form_class = RequestCreateForm
    template_name = 'orders/request_form.html'
    success_url = reverse_lazy('request_list')
    success_message = "Заявка успешно создана!"
