from django.shortcuts import render
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .models import Category , Project , Task
from .forms import ProjectCreateForm , ProjectUpdateForm

# Create your views here.


class ProjectListView(ListView):
    model = Project
    template_name = "index.html"


class ProjectCreateView(CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "create.html"
    success_url = reverse_lazy('index')


class ProjectUpdateView(UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = "update.html"
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.id])


class ProjectDeleteView(DeleteView):
    model = Project
    template_name = "delete.html"
    success_url = reverse_lazy('index')  





class TaskCreateView(CreateView):
    model = Task
    fields = [ 'project' , 'description' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])   # قمنا بأحضار ال project_id لأنه في علاقة مع التاسك


class TaskUpdateView(UpdateView):
    model = Task
    fields = [ 'is_completed' ]
    http_method_names = ['post']

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])  


class TaskDeleteView(DeleteView):
    model = Task

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])  