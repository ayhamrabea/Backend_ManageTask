from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .models import Category , Project , Task
from .forms import ProjectCreateForm

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "index.html"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "create.html"
    success_url = reverse_lazy('index')
