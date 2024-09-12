from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomCreationForm


# Create your views here.
def home(request):
    return render(request, "home.html")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomCreationForm
    success_url = reverse_lazy("home")
