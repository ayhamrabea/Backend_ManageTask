from django.shortcuts import render
from django.urls import reverse_lazy , reverse
from django.views.generic import ListView , CreateView , UpdateView , DeleteView
from .models import Category , Project , Task
from .forms import ProjectCreateForm , ProjectUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin

# Create your views here.


class ProjectListView(LoginRequiredMixin ,ListView):
    model = Project
    ordering = [ '-update_at' ]
    template_name = "index.html"
    paginate_by = 6

    def get_queryset(self):     # add search
        query_set = super().get_queryset()
        where = {'user_id': self.request.user}
        q = self.request.GET.get('q' , None)
        if q:
            where['title__icontains'] = q
        return query_set.filter(**where)


    


class ProjectCreateView(LoginRequiredMixin ,CreateView):
    model = Project
    form_class = ProjectCreateForm
    template_name = "create.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    


class ProjectUpdateView(LoginRequiredMixin , UserPassesTestMixin ,UpdateView):
    model = Project
    form_class = ProjectUpdateForm
    template_name = "update.html"
    
    def test_func(self):
        return self.get_object().user_id == self.request.user.id

    def get_success_url(self):
        return reverse('project_update' , args=[self.object.id])


class ProjectDeleteView(LoginRequiredMixin , UserPassesTestMixin ,DeleteView):
    model = Project
    template_name = "delete.html"
    success_url = reverse_lazy('index')
      
    def test_func(self):
        return self.get_object().user_id == self.request.user.id




class TaskCreateView(LoginRequiredMixin , UserPassesTestMixin ,CreateView):
    model = Task
    fields = [ 'project' , 'description' ]
    http_method_names = ['post']

    def test_func(self):
        project_id = self.request.POST.get('project','')
        return Project.objects.get(pk=project_id).user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])   # قمنا بأحضار ال project_id لأنه في علاقة مع التاسك


class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Task
    fields = [ 'is_completed' ]
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])  


class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin ,DeleteView):
    model = Task
    def test_func(self):
        return self.get_object().project.user_id == self.request.user.id
    
    def get_success_url(self):
        return reverse('project_update' , args=[self.object.project.id])  