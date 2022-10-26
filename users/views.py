from django.views.generic import TemplateView
from .forms import CostumUserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView


# Create your views here.
class SignUpView(CreateView):
    form_class = CostumUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'